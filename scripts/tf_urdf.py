"""
Script for getting transforms between links of a robot from a URDF.
Author: Mayank Mittal
"""
import argparse

import urdfpy
import numpy as np
import scipy.spatial.transform as scipy_tf


if __name__ == '__main__':

    # Parse Args
    parser = argparse.ArgumentParser(
        description='Get transforms between links of a robot from a URDF file'
    )
    parser.add_argument('urdf', type=str,
                        help='Path to URDF file that describes the robot')
    parser.add_argument('link_1', type=str, help='Name of Link 1')
    parser.add_argument('link_2', type=str, help='Name of Link 2')
    args = parser.parse_args()

    # load robot
    robot = urdfpy.URDF.load(args.urdf)
    # get link indices in the robot
    all_links_names = [link.name for link in robot.links]
    print("Found links: ", all_links_names)

    # get link indices in the robot
    base_link_index = all_links_names.index(robot.base_link.name)
    link_1_index = all_links_names.index(args.link_1)
    link_2_index = all_links_names.index(args.link_2)
    # print info
    print('-' * 80)
    print(f"Root  : '{robot.base_link.name}' at index {base_link_index}")
    print(f"Link 1: '{args.link_1}' at index {link_1_index}")
    print(f"Link 2: '{args.link_2}' at index {link_2_index}")

    # get transforms
    fk = robot.link_fk()
    tf_link_1_world = fk[robot.links[link_1_index]]
    tf_link_2_world = fk[robot.links[link_2_index]]
    tf_link_1_link_2 = np.linalg.inv(tf_link_1_world) @ tf_link_2_world

    # get minimal representation of the transform
    tf_link_1_link_2_pos = tf_link_1_link_2[:3, 3]
    tf_link_1_link_2_quat = scipy_tf.Rotation.from_matrix(tf_link_1_link_2[:3, :3]).as_quat()
    # convert quaternion to wxyz
    tf_link_1_link_2_quat = tf_link_1_link_2_quat[[3, 0, 1, 2]]
    # print info
    print('-' * 80)
    print(f"Transform from '{args.link_1}' to '{args.link_2}':")
    print(f"Position         : {tf_link_1_link_2_pos}")
    print(f"Quaternion (wxyz): {tf_link_1_link_2_quat}")
