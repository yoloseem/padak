""":mod:`padak.html5.tags` --- HTML5 tags
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
class Element(object):
    """Base class of all of HTML tags."""

    # The global attributes below can be used on any HTML5 element.
    _global_attributes = (
        'accesskey', 'class', 'contenteditable', 'contextmenu', 'dir',
        'draggable', 'dropzone', 'hidden', 'id', 'lang', 'spellcheck', 'style',
        'tabindex', 'title'
    )
    _global_events_attributes = (
        'onafterprint', 'onbeforeprint', 'onbeforeonload', 'onblur', 'onerror',
        'onfocus', 'onhaschange', 'onload', 'onmessage', 'onoffline',
        'ononline', 'onpagehide', 'onpageshow', 'onpopstate', 'onredo',
        'onresize', 'onstorage', 'onundo', 'onunload',
        'onblur', 'onchange', 'oncontextmenu', 'onfocus', 'onformchange',
        'onforminput', 'oninput', 'oninvalid', 'onselect', 'onsubmit',
        'onkeydown', 'onkeypress', 'onkeyup',
        'onclick', 'ondblclick', 'ondrag', 'ondragend', 'ondragenter',
        'ondragleave', 'ondragover', 'ondragstart', 'ondrop', 'onmousedown',
        'onmousemove', 'onmouseout', 'onmouseover', 'onmouseup', 'onmousewheel',
        'onscroll',
        'onabort', 'oncanplay', 'oncanplaythrough', 'ondurationchange',
        'onemptied', 'onended', 'onerror', 'onloadeddata', 'onloadedmetadata',
        'onloadstart', 'onpause', 'onplay', 'onplaying', 'onprogress',
        'onratechange', 'onreadystatechange', 'onseeked', 'onseeking',
        'onstalled', 'onsuspend', 'ontimeupdate', 'onvolumechange', 'onwaiting'
    )

    def __init__(self, *contents, **kwargs):
        if not hasattr(self, 'tagname'):
            self.tagname = type(self).__name__.lower()
        try:
            self.attrs = kwargs.pop('attrs')
        except KeyError:
            self.attrs = {}
        for k, v in kwargs.iteritems():
            self.attrs[k] = v
        self.content = []
        if len(contents) > 0:
            for c in contents:
                if hasattr(c, '__iter__'):
                    self.content.extend(citem for citem in c)
                else:
                    self.content.append(c)

    def __html__(self):
        args_html = str.join('',
            [' {0}="{1}"'.format(*a) for a in self.attrs.iteritems()])
        if hasattr(self, '_single') and self._single:
            html = '<{0}{1} />'.format(self.tagname, args_html)
        else:
            if hasattr(self, 'content'):
                content_html = []
                if hasattr(self.content, '__iter__'):
                    content_html.extend(
                        c.__html__() if isinstance(c, Element) else str(c) \
                        for c in self.content
                    )
                else:
                    content_html = content_html.append(
                        self.content.__html__() if isinstance(c, Element) \
                                                else str(self.content))
                content_html = '\n'.join(content_html)
            html = '<{0}{1}>{2}</{0}>'.format(self.tagname, args_html,
                                              content_html)
        return html

    @property
    def html(self):
        return self.__html__()

    def __str__(self):
        return self.html

    def __unicode__(self):
        return self.html

    def __repr__(self):
        args_repr = ['{0}={1!r}'.format(*a) for a in self.attrs.iteritems()]
        if hasattr(self, 'content'):
            content_repr = []
            if hasattr(self.content, '__iter__'):
                content_repr.extend(repr(c) for c in self.content)
            else:
                content_repr = content_repr.append(repr(self.content))
            args_repr = content_repr + args_repr
        args_repr = ', '.join(args_repr)
        return '{0}({1})'.format(type(self).__name__, args_repr)


class HTML(Element):
    """<html> tag."""


class A(Element):
    """<a> tag class."""


class Abbr(Element):
    """<abbr> tag class."""


class Acronym(Element):
    """<acronym> tag class."""


class Address(Element):
    """<address> tag class."""


class Applet(Element):
    """<applet> tag class."""


class Area(Element):
    """<area> tag class."""


class Article(Element):
    """<article> tag class."""


class Aside(Element):
    """<aside> tag class."""


class Audio(Element):
    """<audio> tag class."""


class B(Element):
    """<b> tag class."""


class Base(Element):
    """<base> tag class."""


class Basefont(Element):
    """<basefont> tag class."""


class Bdi(Element):
    """<bdi> tag class."""


class Bdo(Element):
    """<bdo> tag class."""


class Big(Element):
    """<big> tag class."""


class Blockquote(Element):
    """<blockquote> tag class."""


class Body(Element):
    """<body> tag class."""


class Br(Element):
    """<br> tag class."""


class Button(Element):
    """<button> tag class."""


class Canvas(Element):
    """<canvas> tag class."""


class Caption(Element):
    """<caption> tag class."""


class Center(Element):
    """<center> tag class."""


class Cite(Element):
    """<cite> tag class."""


class Code(Element):
    """<code> tag class."""


class Col(Element):
    """<col> tag class."""


class Colgroup(Element):
    """<colgroup> tag class."""


class Command(Element):
    """<command> tag class."""


class Datalist(Element):
    """<datalist> tag class."""


class Dd(Element):
    """<dd> tag class."""


class Del(Element):
    """<del> tag class."""


class Details(Element):
    """<details> tag class."""


class Dfn(Element):
    """<dfn> tag class."""


class Dir(Element):
    """<dir> tag class."""


class Div(Element):
    """<div> tag class."""


class Dl(Element):
    """<dl> tag class."""


class Dt(Element):
    """<dt> tag class."""


class Em(Element):
    """<em> tag class."""


class Embed(Element):
    """<embed> tag class."""


class Fieldset(Element):
    """<fieldset> tag class."""


class Figcaption(Element):
    """<figcaption> tag class."""


class Figure(Element):
    """<figure> tag class."""


class Font(Element):
    """<font> tag class."""


class Footer(Element):
    """<footer> tag class."""


class Form(Element):
    """<form> tag class."""


class Fram(Element):
    """<fram> tag class."""


class Framset(Element):
    """<framset> tag class."""


class H1(Element):
    """<h1> tag class."""


class H2(Element):
    """<h2> tag class."""


class H3(Element):
    """<h3> tag class."""


class H4(Element):
    """<h4> tag class."""


class H5(Element):
    """<h5> tag class."""


class H6(Element):
    """<h6> tag class."""


class Head(Element):
    """<head> tag class."""


class Header(Element):
    """<header> tag class."""


class Hgroup(Element):
    """<hgroup> tag class."""


class Hr(Element):
    """<hr> tag class."""


class I(Element):
    """<i> tag class."""


class Iframe(Element):
    """<iframe> tag class."""


class Img(Element):
    """<img> tag class."""


class Input(Element):
    """<input> tag class."""


class Ins(Element):
    """<ins> tag class."""


class Keygen(Element):
    """<keygen> tag class."""


class Kbd(Element):
    """<kbd> tag class."""


class Label(Element):
    """<label> tag class."""


class Legend(Element):
    """<legend> tag class."""


class Li(Element):
    """<li> tag class."""


class Link(Element):
    """<link> tag class."""


class Map(Element):
    """<map> tag class."""


class Mark(Element):
    """<mark> tag class."""


class Menu(Element):
    """<menu> tag class."""


class Meta(Element):
    """<meta> tag class."""


class Meter(Element):
    """<meter> tag class."""


class Nav(Element):
    """<nav> tag class."""


class Noframes(Element):
    """<noframes> tag class."""


class Noscript(Element):
    """<noscript> tag class."""


class Object(Element):
    """<object> tag class."""


class Ol(Element):
    """<ol> tag class."""


class Optgroup(Element):
    """<optgroup> tag class."""


class Option(Element):
    """<option> tag class."""


class Output(Element):
    """<output> tag class."""


class P(Element):
    """<p> tag class."""


class Param(Element):
    """<param> tag class."""


class Pre(Element):
    """<pre> tag class."""


class Progress(Element):
    """<progress> tag class."""


class Q(Element):
    """<q> tag class."""


class Rp(Element):
    """<rp> tag class."""


class Rt(Element):
    """<rt> tag class."""


class Ruby(Element):
    """<ruby> tag class."""


class S(Element):
    """<s> tag class."""


class Samp(Element):
    """<samp> tag class."""


class Script(Element):
    """<script> tag class."""


class Section(Element):
    """<section> tag class."""


class Select(Element):
    """<select> tag class."""


class Small(Element):
    """<small> tag class."""


class Source(Element):
    """<source> tag class."""


class Span(Element):
    """<span> tag class."""


class Strike(Element):
    """<strike> tag class."""


class Strong(Element):
    """<strong> tag class."""


class Style(Element):
    """<style> tag class."""


class Sub(Element):
    """<sub> tag class."""


class Summary(Element):
    """<summary> tag class."""


class Sup(Element):
    """<sup> tag class."""


class Table(Element):
    """<table> tag class."""


class Tbody(Element):
    """<tbody> tag class."""


class Td(Element):
    """<td> tag class."""


class Textarea(Element):
    """<textarea> tag class."""


class Tfoot(Element):
    """<tfoot> tag class."""


class Th(Element):
    """<th> tag class."""


class Thead(Element):
    """<thead> tag class."""


class Time(Element):
    """<time> tag class."""


class Title(Element):
    """<title> tag class."""


class Tr(Element):
    """<tr> tag class."""


class Track(Element):
    """<track> tag class."""


class Tt(Element):
    """<tt> tag class."""


class U(Element):
    """<u> tag class."""


class Ul(Element):
    """<ul> tag class."""


class Var(Element):
    """<var> tag class."""


class Video(Element):
    """<video> tag class."""


class Wbr(Element):
    """<wbr> tag class."""
