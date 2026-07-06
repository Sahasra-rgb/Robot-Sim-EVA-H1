from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import Command
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():

    robot_description = Command([
        'xacro ',
        PathJoinSubstitution([
            FindPackageShare('eva_h1_description'),
            'urdf',
            'eva_h1.urdf.xacro'
        ])
    ])

    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{
            'robot_description': robot_description
        }]
    )

    return LaunchDescription([
        robot_state_publisher
    ])
