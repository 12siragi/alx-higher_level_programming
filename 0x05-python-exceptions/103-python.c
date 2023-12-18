#include <Python.h>
#include <stdio.h>

/* Function prototypes */
void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/* Function definitions */

void print_python_list(PyObject *p) {
    Py_ssize_t size, alloc, i;
    const char *type;
    PyListObject *list = (PyListObject *)p;
    PyVarObject *var = (PyVarObject *)p;

    size = var->ob_size;
    alloc = list->allocated;

    setbuf(stdout, NULL);

    printf("[*] Python list info\n");
    if (strcmp(p->ob_type->tp_name, "list") != 0) {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", alloc);

    for (i = 0; i < size; i++) {
        type = list->ob_item[i]->ob_type->tp_name;
        printf("Element %ld: %s\n", i, type);
    }
}

void print_python_bytes(PyObject *p) {
    Py_ssize_t size, i;
    PyBytesObject *bytes = (PyBytesObject *)p;

    setbuf(stdout, NULL);

    printf("[.] bytes object info\n");
    if (strcmp(p->ob_type->tp_name, "bytes") != 0) {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
    printf("  trying string: %s\n", bytes->ob_sval);

    size = (((PyVarObject *)p)->ob_size >= 10) ? 10 : ((PyVarObject *)p)->ob_size + 1;

    printf("  first %ld bytes: ", size);
    for (i = 0; i < size; i++) {
        printf("%02hhx", bytes->ob_sval[i]);
        if (i == (size - 1))
            printf("\n");
        else
            printf(" ");
    }
}

void print_python_float(PyObject *p) {
    char *buffer = NULL;

    setbuf(stdout, NULL);

    printf("[.] float object info\n");
    if (strcmp(p->ob_type->tp_name, "float") != 0) {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }

    buffer = PyOS_double_to_string(((PyFloatObject *)p)->ob_fval, 'r', 0,
            Py_DTSF_ADD_DOT_0, NULL);
    printf("  value: %s\n", buffer);
    PyMem_Free(buffer);
}
