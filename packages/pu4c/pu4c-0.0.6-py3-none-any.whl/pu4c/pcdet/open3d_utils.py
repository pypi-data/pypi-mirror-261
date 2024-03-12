import open3d as o3d
from pu4c.pcdet.common_utils import color_rings7_det as colormap, read_points
import numpy as np

def translate_boxes_to_open3d_instance(xyz, lwh, rpy):
    """
             4-------- 6
           /|         /|
          5 -------- 3 .
          | |        | |
          . 7 -------- 1
          |/         |/
          2 -------- 0
    """
    rot = o3d.geometry.get_rotation_matrix_from_axis_angle(rpy)
    box3d = o3d.geometry.OrientedBoundingBox(xyz, rot, lwh)

    line_set = o3d.geometry.LineSet.create_from_oriented_bounding_box(box3d)

    lines = np.asarray(line_set.lines)
    lines = np.concatenate([lines, np.array([[1, 4], [7, 6]])], axis=0)

    line_set.lines = o3d.utility.Vector2iVector(lines)

    return line_set, box3d
def create_add_3d_boxes(bboxes_3d, vis=None, with_label=False):
    """
    bboxes_3d: (N, 7)[xyz, lwh, yaw]
    """
    geometries = []
    for box in bboxes_3d:
        line_set, box3d = translate_boxes_to_open3d_instance(box[:3], box[3:6], np.array([0, 0, box[6] + 1e-10]))
        line_set.paint_uniform_color(
            colormap[box[7]] if with_label else [0, 1, 0],
        )
        geometries.append(line_set)
        if vis is not None: vis.add_geometry(line_set)
    return geometries
def playcloud(point_clouds, bboxes_3d=None, # 3d det
              labels=None, label_fn=None, # 3d seg
              start=0, step=10,
              color=None, point_size=None,
              ):
    def switch(vis, i):
        pc = point_clouds[i]
        print(f"frame {i}: {pc['filepath']}")
        vis.clear_geometries()

        axis_pcd = o3d.geometry.TriangleMesh.create_coordinate_frame(size=1.0, origin=[0, 0, 0])
        vis.add_geometry(axis_pcd)

        points = read_points(
            pc['filepath'], num_features=pc['num_features'],
            transmat=pc['transmat'] if pc.get('transmat', None) is not None else None,
            )
        cloud = o3d.geometry.PointCloud()
        cloud.points = o3d.utility.Vector3dVector(points[:, :3])
        if color is not None: cloud.paint_uniform_color(color)
        if point_size: vis.get_render_option().point_size = point_size
        if labels and labels[i]:
            colors = label_fn(labels[i]['filepath'])
            cloud.colors = o3d.utility.Vector3dVector(colors)
        vis.add_geometry(cloud) # 离谱 update 没用，add 反而有效

        if bboxes_3d and bboxes_3d[i]:
            for label, box in zip(bboxes_3d[i]['label'], bboxes_3d[i]['bboxes_3d']):
                line_set, box3d = translate_boxes_to_open3d_instance(box[0:3], box[3:6], np.array([0, 0, box[6]]))
                line_set.paint_uniform_color(colormap[label])
                vis.add_geometry(line_set) # 线框
                # vis.add_geometry(box3d) # 立方体

        # vis.poll_events()
        vis.update_renderer()

    def prev(vis):
        global g_idx
        g_idx = max(g_idx - 1, 0)
        switch(vis, g_idx)
    def next(vis):
        global g_idx
        g_idx = min(g_idx + 1, len(point_clouds)-1)
        switch(vis, g_idx)
    def prev_n(vis):
        global g_idx
        g_idx = max(g_idx - step, 0)
        switch(vis, g_idx)
    def next_n(vis):
        global g_idx
        g_idx = min(g_idx + step, len(point_clouds)-1)
        switch(vis, g_idx)

    vis = o3d.visualization.VisualizerWithKeyCallback()
    vis.create_window()
    vis.get_render_option().point_size = 1.0
    vis.get_render_option().background_color = np.zeros(3)

    vis.register_key_callback(ord('W'), prev_n)
    vis.register_key_callback(ord('S'), next_n)
    vis.register_key_callback(ord('A'), prev)
    vis.register_key_callback(ord('D'), next) # 按小写，但这里要填大写
    # vis.register_key_callback(ord(' '), next) # space

    global g_idx
    g_idx = start
    switch(vis, start)
    vis.run()
    vis.destroy_window()