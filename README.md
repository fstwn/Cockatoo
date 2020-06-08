# COCKATOO

- Cockatoo is a prototypical open-source software toolkit for generating (3d-)knitting patterns from NURBS surface and mesh geometry.
- It is implemented as a [Python](https://www.python.org/) module for use within [McNeel Rhinoceros 6](https://www.rhino3d.com/) aswell as [Grasshopper](https://www.rhino3d.com/6/new/grasshopper).

### [...Yeah, yeah... Knitting... Rhino... Python... I get it. Just tell me how to install and use it!](#installation--usage)

---

## Purpose & Origins

The purpose of this project is to enable Rhino and Grasshopper to derive (3d-)knitting patterns for computerized knitting machines from NURBS surfaces and polygon meshes. The absence of such an open-source toolkit for use directly within conventional CAD-software marks the origin point for this project.

This project constitutes the practical part of my diploma in the [product design department](https://produktdesignkassel.de/) at [Kunsthochschule Kassel](https://www.kunsthochschulekassel.de/).

## Software Structure

- All datastructures, core logic and algorithms are defined in the `cockatoo` python module.
- The [RhinoCommon API](https://developer.rhino3d.com/guides/rhinocommon/what-is-rhinocommon/) is used to handle all geometric operations.
- The `networkx` module is used to handle all the necessary graph operations (for more info, see the [Pecularities](#pecularities) section).
- The `cockatoo` module can be used from within RhinoPython scripts as well as from within Grasshopper through the GHPython scriptable component.
- Cockatoo also includes a set of Grasshopper components (`UserObjects`), which provide a user interface to the underlying python module without the need of scripting.
- The python module as well as the UserObjects are designed to be open for extension.

## Pecularities

- The RhinoPython and GHPython development environments are [very](https://developer.rhino3d.com/guides/rhinopython/what-is-rhinopython/), [very](https://developer.rhino3d.com/guides/rhinopython/ghpython-component/) [special](https://developer.rhino3d.com/guides/rhinopython/python-reference/). I am not going to write in-depth about this here. Everybody who is working with these tools on a regular basis should have come accross their oddities. If not - most information about these topics is available in the [Rhino Developer Docs](https://developer.rhino3d.com/)
- To do all the juicy graph stuff, Cockatoo uses NetworkX. To be more specific, an older version - [NetworkX 1.5](https://networkx.github.io/documentation/networkx-1.5/) is used for... well, [reasons](https://www.grasshopper3d.com/forum/topics/ghpython-ironpython-engine-frames). To prevent problems with dead links and for reasons of simplicity, **this specific networkx module is bundled with Cockatoo**!

## Testing & Contributing

### You are invited to participate (yes - you!)

- Contributing is easy as π (well...easier, actually). Whether you are a designer, student, teacher or scientist working with CNC-knitting - just find out what Cockatoo can do for you. In order to make Cockatoo better, we need real-world testing!
- If Cockatoo doesn't do the things you expected it to do or simply does not work: Tell me about it by [submitting an issue](https://github.com/fstwn/Cockatoo/issues/)!
- To find out more about how you can help testing this software and making it better, have a look at the contribution guidelines.

## Installation & Usage

### 1. Download release files

- Go to [releases](https://github.com/fstwn/Cockatoo/releases) and download the newest release
- Unzip the downloaded archive. You should get two folders: `modules` and `Cockatoo`.

### 2. Install python modules

- Open the scripts folder of Rhino 6 by opening explorer and navigating to
  
  `C:\Users\%USERNAME%\AppData\Roaming\McNeel\Rhinoceros\6.0\scripts`
- Move all the Content from inside the `modules` directory to this scripts folder.

### 3. Install Cockatoo UserObjects

- Navigate to the Grasshopper UserObjects folder. This can be done in two ways:
  - *Either* open explorer and go to
    
    `C:\Users\%USERNAME%\AppData\Roaming\Grasshopper\UserObjects`
  - *Or* open Rhino & Grasshopper and in the Grasshopper Window click on

    `File` >> `Special Folders` >> `User Object Folder`
- Move the whole `Cockatoo` directory to the UserObjects folder.

### 4. Unblock the new UserObjects!

- Go into the `Cockatoo` folder inside Grasshoppers UserObjects folder
- Right click onto the first UserObject and go to **Properties**
- If the text *This file came from another computer [...]* is displayed click on **Unblock**!
- **Unfortunately you have to do this for _EVERY_ UserObject in the folder!**

### 5. Restart Rhino & Grasshopper

- If Rhino was running during the installation process, you'll have to restart it for the changes to take effect!

## Sources & References

This section states the most important sources used in writing this software.

- Popescu, Mariana et al. *[Automated Generation of Knit Patterns for Non-developable Surfaces](https://block.arch.ethz.ch/brg/files/POPESCU_DMSP-2017_automated-generation-knit-patterns_1505737906.pdf)*
- Popescu, Mariana *[KnitCrete - Stay-in-place knitted formworks for complex concrete structures](https://block.arch.ethz.ch/brg/files/POPESCU_2019_ETHZ_PhD_KnitCrete-Stay-in-place-knitted-fabric-formwork-for-complex-concrete-structures_small_1586266206.pdf)*
- Narayanan, Vidya; Albaugh, Lea; Hodgins, Jessica; Coros, Stelian; McCann, James *[Automatic Machine Knitting of 3D Meshes](https://textiles-lab.github.io/publications/2018-autoknit/)*
- Narayanan, Vidya; Wu, Kui et al. *[Visual Knitting Machine Programming](https://textiles-lab.github.io/publications/2019-visualknit/)*
- McCann, James; Albaugh, Lea; Narayanan, Vidya; Grow, April; Matusik, Wojciech; Mankoff, Jen; Hodgins, Jessica *[A Compiler for 3D Machine Knitting](https://la.disneyresearch.com/publication/machine-knitting-compiler/)*
- Hagberg, Aric; Schult, Dan; Swart, Pieter *[NetworkX 1.5](https://networkx.github.io/documentation/networkx-1.5/_downloads/networkx_reference.pdf)*
