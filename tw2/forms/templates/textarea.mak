<%namespace name="tw" module="tw2.core.mako_util"/>\
<textarea ${tw.attrs(attrs=w.attrs)}>${unicode(w.value or '')}</textarea>
