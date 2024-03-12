from . import config

def create_semantic_kitti_vis_infos(root=config.semantic_kitti_root, split='train', num_features=4):
    import os
    from glob import glob
    seq_nums = {
        'train': [0,1,2,3,4,5,6,7,9,10],
        'val': [8],
        'trainval': [0,1,2,3,4,5,6,7,8,9,10],
        'test': [11,12,13,14,15,16,17,18,19,20,21],
    }
    infos = []
    for seq in seq_nums[split]:
        filepaths = sorted(glob(os.path.join(root, 'dataset', 'sequences', str(seq).zfill(2), 'velodyne', '*.bin')))
        for filepath in filepaths:
            filepath = os.path.relpath(filepath, root)
            frame_id = os.path.basename(filepath)[:-4]
            infos.append({
                'lidar': {'frame_id': frame_id, 'filepath': filepath, 'num_features': num_features},
                'label': {'filepath': filepath.replace('velodyne', 'labels')[:-3] + 'label'},
                })
    return infos
def semantic_kitti_label_fn(filepath=None, label=None):
    import numpy as np
    if filepath is not None:
        label = np.fromfile(filepath, dtype=np.uint32).reshape((-1, 1))
        label = label & 0xFFFF  # delete high 16 digits binary
        label = np.vectorize(config.semantic_kitti_class_map.__getitem__)(label).reshape(-1)
    colors = np.array([config.semantic_kitti_colormap_rgb[cls] for cls in label])

    return label, colors
