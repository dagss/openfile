


def openfile(filename):
    # Attempt HDF5
    if filename.endswith('.h5') or filename.endswith('.hdf5'):
        import tables
        f = tables.openFile(filename, 'r')
        try:
            opener = f.getNodeAttr(f.root, 'python_handler')
        finally:
            f.close()
        if '.' not in opener:
            raise ValueError()
        split = opener.rfind('.')
        module = __import__(opener[:split], fromlist=opener[split + 1:])
        func = getattr(module, opener[split + 1:])
        return func(filename)

    # Attempt Python pickle
    from cPickle import load
    try:
        with file(filename) as f:
            return load(f)
        return x
    except:
        pass

    # Give up
    raise NotImplementedError()
        
