#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Double pointer to the head of the linked list.
 *
 * Return: 1 if the linked list is a palindrome, 0 otherwise.
 * An empty list is considered a palindrome.
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL)
	{
		return 1;
	}

	int length = 0;
	listint_t *current = *head;
	while (current != NULL)
	{
		length++;
		current = current->next;
	}

	int stack[length / 2];
	int top = -1;

	current = *head;
	for (int i = 0; i < length / 2; i++)
	{
		stack[++top] = current->n;
		current = current->next;
	}

	if (length % 2 != 0)
	{
		current = current->next;
	}

	while (current != NULL)
	{
		if (current->n != stack[top--])
		{
			return 0;
		}
		current = current->next;
	}

	return 1;
}
