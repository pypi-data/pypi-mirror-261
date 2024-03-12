# PyRosetta installer

Download PyRosetta wheel package from one of www.PyRosetta.org mirrors and install it.

**Note that USE OF PyRosetta FOR COMMERCIAL PURPOSES REQUIRE PURCHASE OF A LICENSE.**
See https://github.com/RosettaCommons/rosetta/blob/main/LICENSE.md or email license@uw.edu for details.

To install PyRosetta, after installing package, run:

```python -c 'import pyrosetta_installer; pyrosetta_installer.install_pyrosetta()'```

The `install_pyrosetta` function also takes few optional arguments:
* `distributed=False` - install PyRosetta with `cxx11thread.serialization` support and also install packages required for `pyrosetta.distributed` framework
* `mirror=0` - mirror to use, default is to use west mirror
* `serialization=False` - install PyRosetta `cxx11thread.serialization` build
* `silent=False` - minimize log outout during installation 
* `skip_if_installed=True` - skip install if existen PyRosetta install detected
* `type='Release'` - PyRosetta build to install: `Release`, `MinSizeRel`
