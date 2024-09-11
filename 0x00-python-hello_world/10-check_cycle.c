#include "lists.h"

/**
 * check_cycle - this function determines whether or not
 * a linked list is a cycle or not
 * @list: the list in question
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *buffer = list;
	listint_t *mask = list;

	if (!list)
		return (0);

	while (buffer && mask && mask->next)
	{
		buffer =  buffer->next;
		mask = mask->next->next;
		if (buffer == mask)
			return (1);
	}
	return (0);
}
