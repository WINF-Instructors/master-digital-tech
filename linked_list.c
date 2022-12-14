#include <stdio.h>
#include <stdlib.h>

struct element
{
    int value;            /* der Wert des Elements          */
    struct element *next; /* Zeiger auf das nächste Element */
};


void printliste(const struct element *e)
{
    for( ; e != NULL ; e = e->next )
    {
        printf("%d\n", e->value);
    }
}


void append(struct element **lst, int value)
{
    struct element *neuesElement;
    
    /* Zeiger auf die Einfügeposition ermitteln, d.h. bis zum Ende laufen */
    while( *lst != NULL ) 
    {
        lst = &(*lst)->next;
    }

    neuesElement = malloc(sizeof(*neuesElement)); /* erzeuge ein neues Element */
    neuesElement->value = value;
    neuesElement->next = NULL; /* Wichtig für das Erkennen des Listenendes     */

    *lst = neuesElement;
}

int main()
{
    struct element *Liste;

    Liste = NULL;      /* init. die Liste mit NULL = leere Liste */
    append(&Liste, 1); /* füge neues Element in die Liste ein    */
    append(&Liste, 3); /* füge neues Element in die Liste ein    */
    append(&Liste, 2); /* füge neues Element in die Liste ein    */

    printliste(Liste); /* zeige alle Elemente der Liste an */

    return 0;
}