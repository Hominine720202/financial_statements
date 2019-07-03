FROM jupyter/datascience-notebook
RUN jupyter notebook --generate-config -y
RUN echo "c.NotebookApp.password='sha1:04385f97bc74:0b5c5596476a0445ba7176c17196db82cc507933'">>/home/jovyan/.jupyter/jupyter_notebook_config.py
RUN pip install python-constraint
RUN pip install numpy
RUN pip install pandas
RUN pip install pydoe
RUN pip install diversipy
USER root
RUN sudo apt-get update
RUN sudo apt-get install -y swig
RUN pip install matplotlib
RUN pip install OApackage