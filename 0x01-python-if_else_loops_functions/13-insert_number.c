#include "lists.h"

/**
 * insert_node - function that inserts number into a sorted singly linked list
 * @head: pointer reference to head of linked list
 * @number: the number i need to insert
 *
 * Return:the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *index = *head, *new_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;

	if (index == NULL || index->n >= number)
	{
		new_node->next = index;
		*head = new_node;
		return (new_node);
	}

	while (index && index->next && index->next->n < number)
			index = index->next;

	new_node->next = index->next;
	index->next = new_node;

	return (new_node);
}
