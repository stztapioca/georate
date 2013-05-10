
def check_node(a,b):
    try:
        node = a.objects.get(pk=b)
    except (a.DoesNotExist):
        print('nuncesta')
    return

def is_participated(node_id):
    from django.core.exceptions import ObjectDoesNotExist
    from nodes.models import Node
    from participation.models import Node_Rating_Count
    n = Node.objects.get(pk=node_id)
    try:
        p=n.node_rating_count
    except ObjectDoesNotExist:
        print('no relation')
        nrc=Node_Rating_Count(node_id=n.id)
        nrc.save()
    return 
    

