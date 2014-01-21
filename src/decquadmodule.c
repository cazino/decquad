#include <Python.h>

static PyObject *
dummy_meth(PyObject *self, PyObject *args)
{
    return PyLong_FromLong(1);
}

static PyObject *DecQuadError;


static PyMethodDef DecQuadMethods[] = {
    {"dummy_meth",  dummy_meth, METH_VARARGS,
     ""},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};


static struct PyModuleDef decquadmodule = {
   PyModuleDef_HEAD_INIT,
   "decquad",   /* name of module */
   NULL, /* module documentation, may be NULL */
   -1,       /* size of per-interpreter state of the module,
                or -1 if the module keeps state in global variables. */
   DecQuadMethods
};

PyMODINIT_FUNC
PyInit_decquad(void)
{
    return PyModule_Create(&decquadmodule);
}