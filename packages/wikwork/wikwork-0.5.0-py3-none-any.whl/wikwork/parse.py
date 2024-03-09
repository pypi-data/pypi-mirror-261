#    Utility functions used for parsing multiple language files
#    Copyright (C) 2024 Ray Griner (rgriner_fwd@outlook.com)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#------------------------------------------------------------------------------

"""Utility functions used for parsing multiple language files."""

#------------------------------------------------------------------------------
# File:    parse.py
# Author:  Ray Griner
# Date:    2024-03-04
# Changes:
#------------------------------------------------------------------------------
__author__ = 'Ray Griner'
#__all__ = ['AudioFile','Headword']

# Standard modules
import re
import logging
import collections
from typing import Optional, Generator, Callable, Dict, Any

WikiTemp = collections.namedtuple('WikiTemp','name params')

logger = logging.getLogger(__name__)

def _put_results_in_attrib(self, entry_index: int,
                 attr: Optional[str], results: list[str]) -> None:
    if entry_index<0:
        #logger.warning('No entry found for %s', self.headword)
        return
    value = '; '.join(results)
    if attr is not None:
        if not hasattr(self.entries[entry_index], attr):
            logger.error('Attribute %s does not exist', attr)
            return
        setattr(self.entries[entry_index], attr, value)

def _one_parameter(self, entry_index: int, attr: str, line: str,
                   param: str) -> None:
    pattern = (r'\|\s*'
               f'{param}'
               r'\s*=(.*?)(\||\}\})')
    regex_match = re.search(pattern, line)
    if regex_match:
        setattr(self.entries[entry_index], attr,
                str.strip(regex_match.group(1)))

#def _one_param_dict(self, entry_index: int, attr: str,
#                    wdict: dict[str, str], param: str) -> None:
#    if param in wdict:
#        setattr(self.entries[entry_index], attr, wdict[param])

def parse_one_template(template: str) -> tuple[Optional[WikiTemp], str]:
    """Parse a string formatted (approximately) as a MediaWiki template.

    Parse the template and extract the name and parameter names/numbers
    and values. For simplicity, the parser will not parse more complicated
    templates, even if they have valid Mediawiki syntax. For example, 
    if a parameter value contains a template, the contained template is
    not parsed or transcluded by the function.
    Function assumes:
        1. The string is a correctly formed template ('{{...}}')
        2. Template name contains alphanumeric characters or '_','-','(',
           ')', ' ', '/'
        3. No unmatched braces or brackets in parameter names or values
        4. Any '=' or '|' inside braces or brackets in parameter names or
           values are not treated as parameter delimiters or name=value
           delimiters in the template being parsed.
        6. Nested templates will not be transcluded or parsed.
        7. Template cannot contain '<nowiki>'.

    Parameters
    ----------
    template : str
        Template to parse

    Returns
    -------
    2-tuple as (str, `WikiTemp`), where the first element is an error
    message if parsing wasn't successful and the second is a `WikiTemp`
    object (if successful) or None if not. The `WikiTemp` object is
    a named tuple with elements `name` and `params`, where `params`
    is a dictionary of the parameter name or number (as str) mapped
    to the parameter value.
    """
    if not template.startswith('{{') or not template.endswith('}}'):
        return (None, "template should look like '{{...}}'")
    if template.find('<nowiki>')>-1:
        return (None, 'Cannot parse template with <nowiki>')
    #if template.find('"') > -1:
    #    return (None, 'Cannot parse template with double quotes')

    name_status = 0  # 0=not started, 1=in middle, 2=done
    name_list: list[str] = []
    space_list: list[str] = []
    name = ''
    param_brace_ctr = 0
    param_bracket_ctr = 0
    # list of characters in parameter name or value, not including leading or
    #  trailing whitespace
    param_list: list[str] = []
    # list of whitespace before first non-whitespace character in parameter
    # name/value
    pre_param_space_list: list[str] = []
    # list of whitespace after last non-whitespace character in parameter
    # name/value. Unlike for template name, we need to preserve both the
    # leading and trailing whitespace for unnamed paramaters, so need two
    # lists.
    post_param_space_list: list[str] = []
    # 0 is prior to first non-whitespace character for parameter name/value
    param_status: int = 0
    # 'part1' = before equal sign, 'part2' is after equal sign
    param_part: str = 'name'
    # dictionary of results
    param_dict: dict[str, str] = {}
    param_number = 1
    param_name: str = ''
    for char in template[2:len(template)-2]:
        # First parse the template name
        if name_status < 2:
            if char.isspace() and name_status == 0:
                pass
            elif char.isspace() and name_status == 1:
                space_list.append(char)
            elif char=='|' and name_status == 0:
                return (None, 'empty template')
            elif char == '|' and name_status == 1:
                name_status = 2
                name = ''.join(name_list)
                param_part = 'part1'
            elif char.isalnum() or char in [' ','-','_','(',')','.', '/']:
                name_status = 1
                for item in space_list:
                    name_list.append(item)
                space_list = []
                name_list.append(char)
            else:
                return (None, 'character not expected in name')
        else:  # Now parsing template parameters
            if char.isspace():
                if param_status == 0:
                    pre_param_space_list.append(char)
                else:
                    post_param_space_list.append(char)
            else:
                param_status = 1
                if char == '{':
                    param_brace_ctr += 1
                    param_list.append(char)
                elif char == '[':
                    param_bracket_ctr += 1
                    param_list.append(char)
                elif char == '}':
                    param_brace_ctr -= 1
                    if param_brace_ctr < 0:
                        return(None, 'unmatched extra right brace')
                    param_list.append(char)
                elif char == ']':
                    param_bracket_ctr -= 1
                    if param_bracket_ctr < 0:
                        return(None, 'unmatched extra right bracket')
                    param_list.append(char)
                elif (char == '|' and param_brace_ctr == 0
                        and param_bracket_ctr == 0):
                    # we have found value. Save parameter name and value to
                    # param_dict and reset the variables used to hold the
                    # spaces and parameter name/value for next parameter
                    if param_part == 'part1':
                        # Values of unnamed parameters preserve leading and
                        # trailing whitespace.
                        dict_val = ''.join(pre_param_space_list +
                            param_list + post_param_space_list)
                        if str(param_number) in param_dict:
                            return (None, f'{param_number=} in template twice')
                        else:
                            param_dict[str(param_number)] = dict_val
                        param_number += 1
                        param_list = []
                        pre_param_space_list = []
                        post_param_space_list = []
                        param_status = 0
                    elif param_part == 'part2':
                        # Values of named parameters don't preserve leading
                        # or trailing whitespace.
                        dict_val = ''.join(param_list)
                        if param_name in param_dict:
                            return (None, f'{param_name=} in template twice')
                        else:
                            param_dict[param_name] = dict_val
                        param_list = []
                        pre_param_space_list = []
                        post_param_space_list = []
                        param_status = 0
                    param_part = 'part1'
                elif (char == '=' and param_part == 'part1'
                        and param_brace_ctr == 0 and param_bracket_ctr == 0):
                    # found parameter name. leading/trailing whitespace are
                    # not part of the name
                    param_part = 'part2'
                    param_name = ''.join(param_list)
                    if re.search(r'=|\|', param_name):
                        return (None, f'{param_name=} contains = or |')
                    param_list = []
                    pre_param_space_list = []
                    post_param_space_list = []
                    param_status = 0
                else:
                    for item in post_param_space_list:
                        param_list.append(item)
                    post_param_space_list = []
                    param_list.append(char)

    name = ''.join(name_list)
    if param_brace_ctr > 0 or param_bracket_ctr > 0:
        return(None, 'unmatched brace or bracket')

    # Same logic as above when finding a '|', but no need to reinitialize the
    #   status variables or lists
    if param_part == 'part1':
        dict_val = ''.join((pre_param_space_list + param_list
                            + post_param_space_list))
        if str(param_number) in param_dict:
            return (None, f'{param_number=} in template twice')
        else:
            param_dict[str(param_number)] = dict_val
    elif param_part == 'part2':
        dict_val = ''.join(param_list)
        if param_name in param_dict:
            return (None, f'{param_name=} in template twice')
        else:
            param_dict[param_name] = dict_val
    return (WikiTemp(name=name, params=param_dict), '')

def _oneline_templates(word: str, text: str) -> Generator[str, None, None]:
    lines = text.splitlines()
    cumlines = []
    cum_open = 0
    cum_close = 0
    for current in lines:
        cum_open += current.count('{')
        cum_close += current.count('}')
        if cum_open == cum_close:
            cumlines.append(current)
            yield ''.join(cumlines)
            cumlines = []
        else:
            cumlines.append(current)
            logger.debug('Word %s: multi-line template', word)
    yield ''.join(cumlines)

def _parse_multi(self, temp_to_attrib_dict: Dict[str, str],
        in_target_lang: Callable[[str], bool],
        out_target_lang: Callable[[str], bool],
        start_new_entry: Callable[[str], bool],
        start_new_attrib: Callable[[str], bool],
        do_on_each_line: Callable[[Any, int, str], None],
        ignore_template: Callable[[str], bool],
        entry_constructor: Callable[[], Any],
        allow_data_after_template: bool,
        process_other_templates: Callable[[Any, str, int], bool]) -> None:
    """Parse the wikitext and put results in the entries attribute.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """

    lines = _oneline_templates(self.headword, self.wikitext)

    in_target_lang_bool: bool = False
    target_lang_counter: int = 0
    entry_index: int = -1
    saved_attr_name: Optional[str] = None
    results: list[str] = []
    for line in lines:
        if in_target_lang(line):
            target_lang_counter += 1
            if in_target_lang_bool:
                _put_results_in_attrib(self, entry_index, saved_attr_name,
                                       results)
            if target_lang_counter>1:
                logger.info('Lang%s, Word %s: L2 heading %d',
                            self.lang_code, self.headword,
                            target_lang_counter)
                in_target_lang_bool = False
            else:
                in_target_lang_bool = True
        elif out_target_lang(line):
            in_target_lang_bool = False

        if start_new_entry(line):
            _put_results_in_attrib(self, entry_index, saved_attr_name, results)
            results = []
            entry_index += 1
            self.entries.append(entry_constructor())
            saved_attr_name = None

        if in_target_lang_bool:
            if start_new_attrib(line):
                # New template, so write contents of results to attribute
                _put_results_in_attrib(self, entry_index, saved_attr_name,
                                       results)
                # Done writing, so process current line
                results = []
                do_on_each_line(self, entry_index, line)
                val = temp_to_attrib_dict.get(line, None)
                if val is not None:
                    saved_attr_name = val
                else:
                    saved_attr_name = None
                    if ignore_template(line):
                        pass
                    elif process_other_templates(self, line, entry_index):
                        pass
                    elif allow_data_after_template:
                        for k, v in temp_to_attrib_dict.items():
                            if line.startswith(k):
                                rest = str.strip(line[len(k):])
                                if rest:
                                    results.append(rest)
                                saved_attr_name = v
                                break
                        if saved_attr_name is None:
                            logger.info('Word %s: Template not handled: %s',
                                        self.headword, line)
                    else:
                        logger.info('Word %s: Template not handled: %s',
                                    self.headword, line)
            else:
                do_on_each_line(self, entry_index, line)
                if line:
                    results.append(line)
    if in_target_lang_bool:
        _put_results_in_attrib(self, entry_index, saved_attr_name, results)

