# -*- coding: utf-8 -*-

import ckan.lib.base as base
from ckan.common import response, _

from .formatters import Formatter


class MetaexportController(base.BaseController):

    def export(self, id, format):
        try:
            fmt = Formatter.get(format)
        except NameError:
            return base.abort(404, _('%s format is not supported') % format)
        data = fmt.extract_data(id)
        response.headers['content-type'] = fmt.get_content_type()
        return base.render(
            'metaexport/{}.html'.format(format), extra_vars=data
        )
