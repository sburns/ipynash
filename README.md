# IPython Notebook & Parallel

This is a combination of IPython notebooks to explain and demonstrate
why the IPython notebook is so powerful.

## Installation

This works of the master (nearing 2.0) branch of IPython.

    $ pip install -r requirements.txt
    $ git clone git@github.com:fperez/nb-slideshow-template.git

This will get you a recent version of IPython which includes, most notably, the "modal" notebook UI. I also cloned Fernando Perez's notebook slideshow repo which includes an installation notebook.

At this point, everything can be done from notebooks, so start the server.

    $ ipython notebook

### Installing the slideshow

In the browser that opened when you started the server, browse to the `nb-slideshow-template` folder and run the `install-support.ipynb` notebook.

## Notebooks

* [01-intro](http://nbviewer.ipython.org/github/sburns/ipynash/blob/master/01-intro.ipynb)
* [02-basics](http://nbviewer.ipython.org/github/sburns/ipynash/blob/master/02-basics.ipynb)
* 03-data (this doesn't render on nbviewer, I've got too many pngs in there :)
* [04-magic](https://raw.github.com/sburns/ipynash/master/04-magic.ipynb)
* [05-arch](https://github.com/sburns/ipynash/blob/master/05-arch.ipynb)
* [06-parallel](http://nbviewer.ipython.org/github/sburns/ipynash/blob/master/06-parallel.ipynb)
* [07-wrapup](http://nbviewer.ipython.org/github/sburns/ipynash/blob/master/07-wrapup.ipynb)

## Hat tips

* Chris Fonnesbeck for his notebook css
* IPython dev team, obviously
