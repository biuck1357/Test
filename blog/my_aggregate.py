from django .db.models import Aggregate,CharField

class GroupConcat(Aggregate):
    function='GROUP_CONCAT'
    template = '%(function)s(%(distinct)s%(experessions)s%(ordering)s%(separator)s)'

    def __init__(self,experession,distinct=False,ordering=None,separator=',',**extra):
        super(GroupConcat,self).__init__(
            experession,
            distinct='DISTINCT ' if distinct else '',
            ordering=' ORDER BY %s' % ordering if ordering is not None else '',
            separator=' SEPARATOR "%s"' % separator,
            output_field=CharField(),
            **extra)