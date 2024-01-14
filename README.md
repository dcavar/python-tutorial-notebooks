# Python Tutorials for NLP, ML, AI

(C) 2016-2024 by [Damir Cavar]

See also: [NLP-Lab](https://nlp-lab.org/) at [Indiana University].


See the licensing details on the individual documents and in the [LICENSE] file in the code folder.


The files in this folder are [Jupyter]-based tutorials for NLP, ML, AI in Python for classes I teach in Computational Linguistics, Natural Language Processing (NLP), Machine Learning (ML), and Artificial Intelligence (AI) at [Indiana University].

If you find this material useful, please cite the author and source (that is [Damir Cavar] and all the sources cited in the relevant notebooks). Please let me know if you have some suggestions on how to correct the notebooks, improve them, or add some material and explanations.


## Introduction

The instructions below are somewhat outdated. I use just [Jupyter-Lab](https://jupyter.org/) now. Follow [the instructions here](https://jupyter.org/install) to set it up on different machine types and operating systems.



To run this material in [Jupyter] you need to have Python 3.x and [Jupyter] installed. You can save yourself some trouble by using the [Anaconda Python 3.x distribution].

Clone the project folder using:

	git clone https://github.com/dcavar/python-tutorial-for-ipython.git

Some of the notebooks may contain code that requires various kinds of [Python] modules to be installed in specific versions. Some of the installations might be complicated and problematic. I am working on a more detailed description of installation procedures and dependencies for each notebook. Stay tuned, this is coming soon.


### Installing Jupyter

[Jupyter] is a great tool for computational publications, tutorials, and exercises. I set up my favorite components for [Jupyter] on Linux (for example [Ubuntu]) this way:

Assuming that I have some of the development tools installed, as for example *gcc*, *make*, etc., I install the packages *python3-pip* and *python3-dev*:

	sudo apt install python3-pip python3-dev

After that I update the global system version of *pip* to the newest version:

	sudo -H pip3 install -U pip

Then I install the newest [Jupyter] and [Jupyterlab] modules globally, updating any previously installed version:

	sudo -H pip3 install -U jupyter jupyterlab

The module that we should not forget is [*plotly*](https://plot.ly/python/):

	sudo -H pip3 install -U plotly

[Scala], [Clojure], and [Groovy] are extremely interesting languages as well, and I love working with [Apache Spark], thus I install [BeakerX] as well. This requires two other [Python] modules: [*py4j*](https://www.py4j.org/) and [*pandas*](https://pandas.pydata.org/). This presupposes that there is an existing Java JDK version 8 or newer already installed on the system. I install all the [BeakerX] related packages:

	sudo -H pip3 install -U py4j
	sudo -H pip3 install -U pandas
	sudo -H pip3 install -U beakerx

To configure and install all [BeakerX] components I run:

	sudo -H beakerx install

Some of the components I like to use require [Node.js]. On [Ubuntu] I usually add the newest [Node.js] as a PPA and not via [Ubuntu Snap]. Some instructions how to achieve that can be found [here](https://tecadmin.net/install-latest-nodejs-npm-on-ubuntu/). To install [Node.js] on [Ubuntu] simply run:

	sudo apt install nodejs

The following commands will add plugins and extensions to [Jupyter] globally:

	sudo -H jupyter labextension install @jupyter-widgets/jupyterlab-manager
	sudo -H jupyter labextension install @jupyterlab/plotly-extension
	sudo -H jupyter labextension install beakerx-jupyterlab

Another useful package is [Voilà], which allows you to turn [Jupyter] notebooks into standalone web applications. I install it using:

	sudo -H pip3 install voila

Now the initial version of the platform is ready to go.

To start the [Jupyter] notebook viewer/editor on your local machine change into the *notebooks* folder within the cloned project folder and run the following command:

	jupyter notebook

A browser window should open up that allows you full access to the notebooks.

Alternatively, check out the instructions how to launch [JupyterLab], [BeakerX], etc.


Enjoy!

[Damir]



[Jupyter]: http://jupyter.org/ "Jupyter"
[JupyterLab]: https://jupyter.org/install "Jupyter"
[Damir Cavar]: http://damir.cavar.me/ "Damir Cavar"
[Damir]: http://damir.cavar.me/ "Damir Cavar"
[LICENSE]: https://github.com/dcavar/python-tutorial-for-ipython/blob/master/LICENSE "License"
[Computational Linguistics Program]: http://cl.indiana.edu/programs.html "IU Computational Linguistics"
[Department of Linguistics]: http://www.indiana.edu/~lingdept/ "IU Department of Linguistics"
[Indiana University]: https://www.indiana.edu/ "Indiana University"
[Anaconda Python 3.x distribution]: https://www.continuum.io/downloads "Anaconda Python"
[BeakerX]: http://beakerx.com/ "BeakerX"
[Scala]: https://www.scala-lang.org/ "The Scala Programming Language"
[Clojure]: https://clojure.org/ "Clojure"
[Groovy]: https://groovy-lang.org/ "Apache Groovy"
[Apache Spark]: https://spark.apache.org/ "Apache Spark"
[Node.js]: https://nodejs.org/en/ "Node.js"
[Ubuntu]: https://ubuntu.com/ "Ubuntu"
[Voilà]: https://voila.readthedocs.io/en/stable/install.html "Voilà"
[Ubuntu Snap]: https://ubuntu.com/tutorials/basic-snap-usage#1-introduction "Ubuntu Snap"
