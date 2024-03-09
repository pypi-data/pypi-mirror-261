def in_jupyter_notebook():
    try:
        from IPython import get_ipython

        # If 'get_ipython' does not return None, we are in an IPython or Jupyter environment
        if get_ipython() is not None:
            return True
    except ImportError:
        # 'IPython' is not available, so definitely not in a Jupyter notebook
        return False

    return False
