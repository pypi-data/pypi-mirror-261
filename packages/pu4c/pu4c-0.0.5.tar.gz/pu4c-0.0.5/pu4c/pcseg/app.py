from . import config

def create_vis_infos(dataset="semantic_kitti", split="val"):
    from .utils import misc_utils
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

    from ..pcdet.utils.open3d_utils import playcloud
    from .utils import misc_utils
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
