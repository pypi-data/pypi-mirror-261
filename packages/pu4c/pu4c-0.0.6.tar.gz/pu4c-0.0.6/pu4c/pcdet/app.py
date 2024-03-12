from . import config

def create_vis_infos(dataset="kitti", split="val", info_pkl=None, add_ext_info=False):
    """
    生成用于可视化的数据接口
    Examples:
        pu4c.pcdet.app.create_vis_infos("kitti", "train", "/datasets/blob/pcdet/data/kitti/kitti_infos_train.pkl")
        pu4c.pcdet.app.create_vis_infos("nuscenes", "train", "/datasets/blob/pcdet/data/nuscenes/v1.0-trainval/nuscenes_infos_10sweeps_train.pkl", add_ext_info=True)
        pu4c.pcdet.app.create_vis_infos("waymo", "train", "/datasets/blob/mmdet3d/data/waymo/kitti_format/waymo_infos_train.pkl", add_ext_info=True)
    """
    from . import misc_utils
    import pickle
    if hasattr(misc_utils, f'create_{dataset}_vis_infos'):
        if dataset in ['kitti', 'nuscenes', 'waymo']:
            assert(info_pkl is not None)
            vis_infos = getattr(misc_utils, f'create_{dataset}_vis_infos')(pkl=info_pkl, add_ext_info=add_ext_info)
        elif info_pkl is None:
            vis_infos = getattr(misc_utils, f'create_{dataset}_vis_infos')(split=split)
        vis_info_pkl = f"/tmp/pu4c/{dataset}_vis_infos_{split}.pkl"
        with open(vis_info_pkl, 'wb') as f:
            pickle.dump(vis_infos, f)
        print(f"create {vis_info_pkl}")
    elif info_pkl is not None:
        import shutil
        vis_info_pkl = f"/tmp/pu4c/{dataset}_vis_infos_{split}.pkl"
        shutil.copy(info_pkl, vis_info_pkl)
        print(f"copy {info_pkl} to {vis_info_pkl}")
def playdataset(dataset="kitti", split="val",
                valid_classes=config.kitti_classes[:3],
                start=0, step=10,
                color=None, point_size=1,
                ):
    """
    visualize dataset split，A/D switch one frame ; W/S switch ${step} frame; esc to exit
    Examples:
        pu4c.pcdet.app.playdataset(dataset="kitti", split="val", valid_classes=pu4c.pcdet.config.kitti_classes[:3])
        pu4c.pcdet.app.playdataset(dataset="nuscenes", split="val", valid_classes=pu4c.pcdet.config.nuscenes_classes[:4])
        pu4c.pcdet.app.playdataset(dataset="kitti", split="val", valid_classes=['Car', 'Van'])
    """
    import pickle
    import numpy as np
    
    vis_info_pkl = f"/tmp/pu4c/{dataset}_vis_infos_{split}.pkl"
    infos = pickle.load(open(vis_info_pkl, 'rb'))

    from .open3d_utils import playcloud
    root = getattr(config, f'{dataset}_root')
    point_clouds, bboxes_3d = [], []
    map_cls_name2id = {cls:i for i, cls in enumerate(valid_classes)}
    for info in infos:
        info['lidar']['filepath'] = f"{root}/{info['lidar']['filepath']}"
        point_clouds.append(info['lidar'])

        if 'annos' in info:
            mask = np.array([name in valid_classes for name in info['annos']['name']], dtype=bool)
            info['annos']['name'] = info['annos']['name'][mask]
            label = [map_cls_name2id[name] for name in info['annos']['name']]
            bboxes_3d_frame = info['annos']['gt_boxes_lidar'][mask]
            bboxes_3d.append({'label': label, 'bboxes_3d': bboxes_3d_frame})
        else:
            bboxes_3d.append(None)

    print(f"visualize {dataset} {split}, total {len(infos)} frames")
    playcloud(point_clouds, bboxes_3d=bboxes_3d, 
              start=start, step=step, color=color, point_size=point_size,
              )


def cloud_viewer_from_dir(root, pattern="*",
                          num_features=4, start=0, step=10, 
                          color=None, point_size=1,
                          ):
    """
    Visualize point clouds in a directory
    """
    from .open3d_utils import playcloud
    from glob import glob
    files = sorted(glob(f'{root}/{pattern}'))

    point_clouds = []
    for filepath in files:
        point_clouds.append({
            'filepath': filepath,
            'num_features': num_features,
        })
    
    playcloud(point_clouds, start=start, step=step, 
              color=color, point_size=point_size,
              )
def cloud_viewer(filepath=None, num_features=4,
                 points=None,
                 point_size=1, transmat=None, color=None,
                 bboxes_3d=None, with_label=False,
                 ):
    """
    快速查看单帧点云，支持 pcd/bin/npy/pkl
    pu4c.pcdet.app.cloud_viewer(filepath, num_features=4, point_size=1)
    pu4c.pcdet.app.cloud_viewer(points, bboxes_3d=bboxes_3d, point_size=1)
    """
    import open3d as o3d
    from .common_utils import read_points
    from .open3d_utils import create_add_3d_boxes
    import numpy as np

    vis = o3d.visualization.Visualizer()
    vis.create_window()
    vis.get_render_option().point_size = point_size
    vis.get_render_option().background_color = np.zeros(3)

    axis_pcd = o3d.geometry.TriangleMesh.create_coordinate_frame(size=1.0, origin=[0, 0, 0])
    vis.add_geometry(axis_pcd)

    if filepath is not None:
        points = read_points(filepath, num_features=num_features, transmat=transmat)
    elif points is None:
        raise ValueError(f"filepath and points cannot both be None")
    cloud = o3d.geometry.PointCloud()
    cloud.points = o3d.utility.Vector3dVector(points[:, :3])
    if color is not None: cloud.paint_uniform_color(color)
    vis.add_geometry(cloud)

    if bboxes_3d is not None:
        create_add_3d_boxes(bboxes_3d, vis=vis, with_label=with_label)

    vis.run()
    vis.destroy_window()


def check_var(var, new=True, path='/tmp/pu4c/check_var.pkl'):
    """
    保存变量到文件，或者将变量与暂存到文件的变量进行对比
    """
    from .common_utils import is_equal_var
    import pickle
    if new:
        pickle.dump(var, open(path, 'wb'))
        print(f"save var to {path}")
    else:
        stage_var = pickle.load(open(path, 'rb'))
        print(is_equal_var(var, stage_var))