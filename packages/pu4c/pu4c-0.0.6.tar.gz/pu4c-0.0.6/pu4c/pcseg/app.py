from . import config

def create_vis_infos(dataset="semantic_kitti", split="val"):
    from . import misc_utils
    import pickle
    if hasattr(misc_utils, f'create_{dataset}_vis_infos'):
        vis_infos = getattr(misc_utils, f'create_{dataset}_vis_infos')(split=split)
        vis_info_pkl = f"/tmp/pu4c/{dataset}_vis_infos_{split}.pkl"
        with open(vis_info_pkl, 'wb') as f:
            pickle.dump(vis_infos, f)
        print(f"create {vis_info_pkl}")
def playdataset(dataset='semantic_kitti', split='val', 
                start=0, step=10,
                ):
    import pickle, os
    vis_info_pkl = f"/tmp/pu4c/{dataset}_vis_infos_{split}.pkl"
    infos = pickle.load(open(vis_info_pkl, 'rb'))

    from ..pcdet.open3d_utils import playcloud
    from . import misc_utils
    root = getattr(config, f'{dataset}_root')
    point_clouds, labels = [], []
    for info in infos:
        info['lidar']['filepath'] = os.path.join(root, info['lidar']['filepath'])
        info['label']['filepath'] = os.path.join(root, info['label']['filepath'])
        point_clouds.append(info['lidar'])
        labels.append(info['label'])

    print(f"visualize {dataset} {split}, total {len(infos)} frames")
    playcloud(point_clouds, 
              labels=labels, label_fn=getattr(misc_utils, f'{dataset}_label_fn'),
              start=start, step=step,
              )


def cloud_viewer(filepath=None, points=None, num_features=4, transmat=None,
                 labelpath=None, label=None, labeltype="semantic_kitti", 
                 point_size=1, color=None,
                 ):
    """
    快速查看单帧点云与语义标签，支持文件路径或读取好的 numpy 数组作为点云或标签输入
    Examples:
        pu4c.pcseg.app.cloud_viewer(filepath, num_features=4, point_size=1) # 查看点云
        pu4c.pcseg.app.cloud_viewer(filepath="/datasets/SemanticKITTI/dataset/sequences/00/velodyne/000000.bin", labelpath="/datasets/SemanticKITTI/dataset/sequences/00/labels/000000.label") # 查看点云及其语义标签
        pu4c.pcseg.app.cloud_viewer(filepath="/datasets/SemanticKITTI/dataset/sequences/08/velodyne/000000.bin", labelpath=["/datasets/SemanticKITTI/dataset/sequences/08/labels/000000.label", "/root/work/000000.label"]) # 查看点云及其两个语义标签差异部分
    """
    import open3d as o3d
    from ..pcdet import read_points
    from . import misc_utils
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
    if labelpath or label:
        label_fn = getattr(misc_utils, f'{labeltype}_label_fn')
        if isinstance(labelpath, list):
            assert(len(labelpath) == 2) # 只允许最多输入两个标签文件，则可视化两个标签文件的差异部分
            label_a, _ = label_fn(filepath=labelpath[0])
            label_b, _ = label_fn(filepath=labelpath[1])
            label_diff = (label_a == label_b).astype(np.int32)
            color_map = [[255, 255, 0], [255, 255, 255]]
            colors = np.array([color_map[cls] for cls in label_diff])
            cloud.colors = o3d.utility.Vector3dVector(colors)
        else:
            label, colors = label_fn(filepath=labelpath, label=label)
            cloud.colors = o3d.utility.Vector3dVector(colors)
             

    if color is not None: cloud.paint_uniform_color(color)
    vis.add_geometry(cloud)

    vis.run()
    vis.destroy_window()