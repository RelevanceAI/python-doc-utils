# python-doc-utils
Utilies for documents including accessing, writing and bulk editing in Python

### Installation 

To install this utility, run the following: 

```
pip install document-utils
```

### To use

```python
from doc_utils import DocUtils

class Encoder(DocUtils):
    """Any class instantiation that may want
    document navigation
    """
```

## Package Usage 

When we want to access field values, we often do this:

`d["field1"]["field2"]`
However, this can cause a number of problems. 
For example - if field2 is missing from field 1 - it would error. 

This package allows you to access nested fields using dot notation. For e.g. 

`get_field("field1.field2", d)` is the equivalent of the above.

Alternatively: 

`d["field1.field2"]`

`get_field(d, "field2.field2")`

The reason why we want to use this is because when we write functions 
that are field-independent, we want to be able to loop through each field. 

For example: 

```{python}

def add_field_suffix(documents, field):
    """Add 'xyz' to a field
    """
    return documents[field] + '-xyz'

This would be impossible if the field was nested!

However, if you ran this: 

```{python}

def add_field_suffix(documents, field):
    """Add 'xyz' to a field 
    """
    return self.get_field(d, field) + "-xyz"
```

Baed on the above function, you can now run it across `field1.field2` as well!


### TODO

- Enable more versatile functionality for document navigation
