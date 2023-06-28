#include <stdio.h>
#include <float.h>
#include <Python.h>

/**
 * print_python_list - Prints information about Python lists
 * @p: Pointer to the Python object
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t i, size;
	PyObject *obj;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	size = PyList_Size(p);
	for (i = 0; i < size; i++)
	{
		obj = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(obj)->tp_name);
	}
}

/**
 * print_python_bytes - Prints information about Python bytes objects
 * @p: Pointer to the Python object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t i, size;
	char *string;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	string = PyBytes_AsString(p);

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);
	printf("  first %ld bytes:", (size < 10) ? size + 1 : 10);
	for (i = 0; i <= size && i < 10; i++)
		printf(" %02hhx", string[i]);
	printf("\n");
}

/**
 * print_python_float - Prints information about Python float objects
 * @p: Pointer to the Python object
 */
void print_python_float(PyObject *p)
{
	PyObject *repr;

	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	repr = PyObject_Repr(p);
	printf("  value: %s\n", PyUnicode_AsUTF8(repr));
	Py_DECREF(repr);
}
