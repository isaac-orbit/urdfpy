"""
Script for getting all parent link names for a given link of a robot from a URDF.
Author: Mayank Mittal
"""
import argparse

import urdfpy


if __name__ == '__main__':

    # Parse Args
    parser = argparse.ArgumentParser(
        description='Get all parent link names for a given link of a robot from a URDF file'
    )
    parser.add_argument('urdf', type=str,
                        help='Path to URDF file that describes the robot')
    parser.add_argument('link', type=str, help='Name of Link')
    args = parser.parse_args()

    # load robot
    robot = urdfpy.URDF.load(args.urdf)
    # get link indices in the robot
    all_links_names = [link.name for link in robot.links]
    print("Found links: ", all_links_names)

    # get all parents of a link
    parent_links = list()
    current_link = args.link
    print('-' * 80)

    def get_parent_link(current_link):
        for joint in robot.joints:
            if joint.child == current_link:
                print(f"Parent of '{current_link}' -> '{joint.parent}'")
                return joint.parent

    while current_link != robot.base_link.name:
        current_link = get_parent_link(current_link)
        parent_links.append(current_link)

    print('-' * 80)
    print(f"All parents of '{args.link}': {parent_links}")
