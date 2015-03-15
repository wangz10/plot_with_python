# Plotting in Python
Scripts and data used for the "Computer Programming for Big Data Biomedicine" class
## Before the class

## Why Python?
+ Elegant syntax
	- concise, human-readable
+ Extensive ranges of applications supported by third-party modules (packages)
	- Web development
	- Database
	- **Scientific computing**
	- Game development
## Import packages
![essays](essays.png)
## Installing Python packages
+ Where to find them?
	- Official website of the package
	- [Python Package Index(PyPI)](https://pypi.python.org/pypi)
	- A large collection of Windows binaries: [http://www.lfd.uci.edu/~gohlke/pythonlibs](http://www.lfd.uci.edu/~gohlke/pythonlibs/)
	- Source code repositories: [GitHub](https://github.com/), [Bitbucket](https://bitbucket.org/)
+ Types and install instructions:
	- Registered on PyPI: `pip install package`
	- .whl file: `pip install package.whl`
	- A directory with setup.py file: `python setup.py install`
	- .exe Windows binary: double click and follow the instructions
## Plotting libraries in python
+ [Matplotlib](http://matplotlib.org/index.html)
	- The basic and stable 2D plotting library
	- Similar to MATLAB
	- Highly customizable figures
+ [ggplot](http://ggplot.yhathq.com/)
	- Professional looking figures
	- Similar to R’s ggplot2
+ [Seaborn](http://stanford.edu/~mwaskom/software/seaborn/#) (statistical data visualization)
	- Wrapper of Matplotlib
	- high-level interface for drawing attractive statistical graphics
+ [Mpld3](http://mpld3.github.io/index.html)
	- Bring together matplotlib and [d3.js](http://d3js.org/)
	- Convert matplotlib figures to interactive web compatible figures
## Get some data to plot
+ Download everything here: 
	- [https://github.com/wangz10/plot_with_python](https://github.com/wangz10/plot_with_python)
+ How to import packages
## Numpy N-dementional array
+ A multidimensional container of items of the same type and size
+ Efficient for indexing and arithmetic operations
+ Creation:
	- From Python array_like objects: `lists`, `tuples` 
	- Intrinsic numpy functions: `np.arange`, `np.zeros`
	- From files: `np.loadtxt`
+ Indexing
## Hands on
refer to the notebook
## Thanks for your attention!
+ Questions?
	- [zichen.wang@mssm.edu](mailto:zichen.wang@mssm.edu)
	