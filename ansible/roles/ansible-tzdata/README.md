Ansible Role for Timezone
=========================

[![Build Status](https://travis-ci.org/pantarei/ansible-role-tzdata.svg?branch=master)](https://travis-ci.org/pantarei/ansible-role-tzdata)
[![GitHub tag](https://img.shields.io/github/tag/pantarei/ansible-role-tzdata.svg)](https://github.com/pantarei/ansible-role-tzdata)
[![GitHub license](https://img.shields.io/github/license/pantarei/ansible-role-tzdata.svg)](https://github.com/pantarei/ansible-role-tzdata/blob/master/LICENSE)

Ansible Role for Timezone Management.

Requirements
------------

This role require Ansible 2.0 or higher.

This role was designed for Ubuntu Server 14.04 LTS and Ubuntu Server 16.04 LTS.

Role Variables
--------------

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th>parameter</th>
<th>required</th>
<th>default</th>
<th>choices</th>
<th>comments</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>tzdata_timezone</td>
<td>yes</td>
<td>Etc/UTC</td>
<td></td>
<td>Time zone in the <a href="https://en.wikipedia.org/wiki/Tz_database">tz database</a>, see <a href="https://en.wikipedia.org/wiki/List_of_tz_database_time_zones">list of time zones</a> for more information.</td>
</tr>
</tbody>
</table>

Dependencies
------------

No additional role dependencies.

Example Playbook
----------------

    - hosts: all
      roles:
        - role: hswong3i.tzdata
          tzdata_timezone: "Asia/Hong_Kong"

License
-------

-   Code released under [MIT](https://github.com/pantarei/ansible-role-tzdata/blob/master/LICENSE)
-   Docs released under [CC BY 4.0](http://creativecommons.org/licenses/by/4.0/)

Author Information
------------------

-   Wong Hoi Sing Edison
    -   <a href="https://twitter.com/hswong3i" class="uri" class="uri">https://twitter.com/hswong3i</a>
    -   <a href="https://github.com/hswong3i" class="uri" class="uri">https://github.com/hswong3i</a>
