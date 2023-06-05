#include "lists.h"

/**
 * check_cycle - checks if it has a cycle
 * list : linked list
 * Return:  1 if there cycle else 0
 */

int check_cycle(listint_t* list) {
	listint_t* slow = list;
	listint_t* fast = list;

	while (fast != NULL && fast->next != NULL) {
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return 1;
	}

	return 0;
}
