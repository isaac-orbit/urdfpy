# Urdfpy

<!-- [![Build Status](https://travis-ci.org/mmatl/urdfpy.svg?branch=master)](https://travis-ci.org/mmatl/urdfpy) -->
[![Documentation Status](https://readthedocs.org/projects/urdfpy/badge/?version=latest)](https://urdfpy.readthedocs.io/en/latest/?badge=latest)
[![Coverage Status](https://coveralls.io/repos/github/mmatl/urdfpy/badge.svg?branch=master)](https://coveralls.io/github/mmatl/urdfpy?branch=master)
[![PyPI version](https://badge.fury.io/py/urdfpy.svg)](https://badge.fury.io/py/urdfpy)

Urdfpy is a simple and easy-to-use library for loading, manipulating, saving,
and visualizing URDF files.

Extensive API documentation is provided [here](https://urdfpy.readthedocs.io/en/latest/).

<p float="left">
  <img src="https://github.com/mmatl/urdfpy/blob/master/docs/source/_static/robotiq.gif?raw=true" alt="GIF of Viewer" width="300"/>
  <img src="https://github.com/mmatl/urdfpy/blob/master/docs/source/_static/ur5.gif?raw=true" alt="GIF of Viewer" width="300"/>
</p>

## Installation

You can install urdfpy directly from pip.

```bash
pip install urdfpy
```

## User Guide

Please see the user guide [here](https://urdfpy.readthedocs.io/en/latest/examples/index.html) for
more information.

---

## Changelog

Compared to the public version of this repository, this fork makes the following changes:

* Makes the joint velocity and effort tags optional. If these tags are missing, then default values are exported into the generated URDF. The default value can be altered through:

```python
import urdfpy

urdfpy.JointLimit._DEFAULT_JOINT_VELOCITY = 80.0
urdfpy.JointLimit._DEFAULT_JOINT_EFFORT = 80.0
```

* Makes exporting of the meshes when saving the URDF file option:

```python
import urdfpy

urdfpy.Mesh._EXPORT_MESH = False
```

* Adds ability to add the tag for [SDF collision](https://www.graphicon.ru/html/2003/Proceedings/Technical/paper495.pdf) to all collision geometries in the URDF. This is used by simulators such as Isaac Gym:

```python
from urdfpy import URDF, SignedDistanceField

# resolution for SDF baking
resolution = 256

robot = URDF.load(input_urdf_file)
# pass all links
for link in robot.links:
    for collision in link.collisions:
        collision.sdf = SignedDistanceField(resolution)
# save the file
output_urdf_file = os.path.join(os.path.dirname(input_urdf_file), output_name)
robot.save(output_urdf_file)
```

The generated URDF will have the additional tag `<sdf>`:

```xml
<collision>
  <origin xyz="..." rpy="..."/>
  <geometry>
    <mesh filename="..."/>
  </geometry>
  <sdf resolution="256"/>
</collision>
```
