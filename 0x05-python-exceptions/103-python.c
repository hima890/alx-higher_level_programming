#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Print information about Python lists
 * @p: Pointer to a PyObject
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t i, size;
	PyObject *item;

	if (!PyList_Check(p))
	{
		printf("[*] Python list info\n  [ERROR] Invalid List Object\n");
		return;
	}

	size = PyList_Size(p);

	printf("[*] Python list info\n[*] Size of the Python List
	 = %ld\n[*] Allocated = %ld\n", size, ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
		if (PyFloat_Check(item))
			print_python_float(item);
	}
}

/**
 * print_python_bytes - Print information about Python bytes
 * @p: Pointer to a PyObject
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t i, size;
	char *str;

	if (!PyBytes_Check(p))
	{
		printf("[.] bytes object info\n  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	str = PyBytes_AsString(p);

	printf("[.] bytes object info\n  size: %ld\n  trying string:
	 %s\n  first %ld bytes: ", size, str, (size < 10) ? size + 1 : 10);

	for (i = 0; i < size && i < 10; i++)
	{
		printf("%02hhx", str[i]);
		if (i < size - 1 && i < 9)
			printf(" ");
	}
	printf("\n");
}

/**
 * print_python_float - Print information about Python float
 * @p: Pointer to a PyObject
 */
void print_python_float(PyObject *p)
{
	if (!PyFloat_Check(p))
	{
		printf("[.] float object info\n  [ERROR] Invalid Float Object\n");
		return;
	}

	printf("[.] float object info\n  value: %f\n", ((PyFloatObject *)p)->ob_fval);
}
