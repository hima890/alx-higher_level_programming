#include <Python.h>

/**
 * print_python_list - Print information about a Python list object.
 * @p: PyObject representing the list object.
 *
 * Description:
 *   This function prints information about a Python list object, including its
 *   size, allocated space, and the type of each element in the list.
 *
 * Parameters:
 *   - p: PyObject representing the Python list object.
 *
 * Note:
 *   If the given object is not a valid list object, an error message
 *  is printed.
 *
 * Example Usage:
 *   PyObject *listObject = PyList_New(3);
 *   PyList_SetItem(listObject, 0, PyLong_FromLong(42));
 *   PyList_SetItem(listObject, 1, PyUnicode_FromString("Hello"));
 *   PyList_SetItem(listObject, 2, PyFloat_FromDouble(3.14));
 *   print_python_list(listObject);
 *   Py_XDECREF(listObject);
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t i, size;
	PyObject *element;

	if (!PyList_Check(p))
	{
		PyErr_Print();
		return;
	}

	size = PyList_Size(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		element = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);
	}
}

/**
 * print_python_bytes - Print information about a Python bytes object.
 * @p: PyObject representing the bytes object.
 *
 * Description:
 *   This function prints information about aPython bytes object, including its
 *   size, string representation, and the first 10 bytes in hexadecimal format.
 *
 * Parameters:
 *   - p: PyObject representing the Python bytes object.
 *
 * Note:
 *   If the given object is not a valid bytesobject, an error message
 *  is printed.
 *
 * Example Usage:
 *   PyObject *bytesObject = PyBytes_FromStringAndSize("Hello, World!", 13);
 *   print_python_bytes(bytesObject);
 *   Py_XDECREF(bytesObject);
*/
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *str;

	if (!PyBytes_Check(p))
	{
		printf("[.] bytes object info\n");
		printf("  [ERROR] Invalid Bytes Object\n");
		PyErr_Print();
		return;
	}

	size = PyBytes_Size(p);
	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);

	str = PyBytes_AsString(p);
	printf("  trying string: %s\n", str);

	printf("  first 10 bytes: ");
	for (i = 0; i < size && i < 10; i++)
	{
		printf("%02x ", str[i] & 0xff);
	}
	printf("\n");
}
