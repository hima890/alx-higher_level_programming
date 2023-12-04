#include <stddef.h>
#include "lists.h"

/**
* is_palindrome - checks if a singly linked list is a palindrome
* @head: pointer to the head of the list
* Return: 0 if not a palindrome, 1 if a palindrome
*/
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *prev_slow, *mid, *second_half;
	int is_palindrome = 1;

	if (!(*head) || !((*head)->next))
		return (1);
	slow = *head;
	fast = *head;
	prev_slow = *head;
	mid = NULL;
	while (fast && fast->next)
	{
		fast = fast->next->next;
		prev_slow = slow;
		slow = slow->next;
	}
	if (fast)
	{
		mid = slow;
		slow = slow->next;
	}
	second_half = slow;
	prev_slow->next = NULL;
	reverse_list(&second_half);
	is_palindrome = compare_lists(*head, second_half);
	reverse_list(&second_half);
	if (mid)
	{
		prev_slow->next = mid;
		mid->next = second_half;
	}
	else
		prev_slow->next = second_half;

	return (is_palindrome);
}

/**
* reverse_list - reverses a linked list
* @head: pointer to the head of the list
*/
void reverse_list(listint_t **head)
{
	listint_t *prev = NULL, *current = *head, *next;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}

/**
* compare_lists - compares two linked lists
* @list1: pointer to the first list
* @list2: pointer to the second list
* Return: 1 if lists are identical, 0 otherwise
*/
int compare_lists(listint_t *list1, listint_t *list2)
{
	while (list1 && list2)
	{
		if (list1->n == list2->n)
		{
			list1 = list1->next;
			list2 = list2->next;
		}
		else
			return (0);
	}

	if (!list1 && !list2)
		return (1);

	return (0);
}
