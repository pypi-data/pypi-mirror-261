Limbo
=====

A `Slack <https://slack.com/>`__ chatbot
----------------------------------------

Status
------

At the moment, I consider limbo to be feature complete, and the project
is in maintenance mode. Every once in a while I come in and update the
dependencies.

Contributions will be considered and may be accepted, you may want to
`email me <bill@billmill.org>`__ because I might not notice your PR.

Python Versions
---------------

At the moment, this software only officially supports python >=3.10,
because the test fixtures fail on older versions of python due to an
urllib3 inconsistency I don’t understand.

It should still run on other versions of python, but for the moment
they’re unfortunately not tested.

Installation
------------

1. Clone the repo
2. `Create a bot user <https://my.slack.com/services/new/bot>`__ if you
   don’t have one yet, and copy the API Token
3. export SLACK_TOKEN=“your-api-token”
4. ``make run`` (or ``make repl`` for local testing)
5. Invite Limbo into any channels you want it in, or just message it in
   #general. Try typing ``!gif dubstep cat`` to test it out

.. figure:: http://i.imgur.com/xhmD6QO.png
   :alt: kitten mittens

   kitten mittens

I recommend that you always run limbo in a
`virtualenv <http://docs.python-guide.org/en/latest/dev/virtualenvs/>`__
so that you are running in a clean environment.

Command Arguments
-----------------

-  ``--test``, ``-t``: Enter command line mode to enter a limbo repl.
-  ``--hook``: Specify the hook to test. (Defaults to “message”).
-  ``-c``: Run a single command.
-  ``--database``, ``-d``: Where to store the limbo sqlite3 database.
   Defaults to limbo.sqlite3.
-  ``--pluginpath``, ``-pp``: The path where limbo should look to find
   its plugins (defaults to /plugins).
-  ``--version``, ``-v``: Print a version number and exit

Environment Variables
---------------------

-  SLACK_TOKEN: Slack API token. Required.
-  LIMBO_LOGLEVEL: The logging level. Defaults to INFO.
-  LIMBO_LOGFILE: File to log info to. Defaults to none.
-  LIMBO_LOGFORMAT: Format for log messages. Defaults to
   ``%(asctime)s:%(levelname)s:%(name)s:%(message)s``.
-  LIMBO_PLUGINS: Comma-delimited string of plugins to load. Defaults to
   loading all plugins in the plugins directory (which defaults to
   “limbo/plugins”)

Note that if you are getting an error message about not seeing
environment variables, you may be running limbo as ``sudo``, which will
clear the environment. Use a virtualenv and always run limbo as a user
process!

Commands
--------

It’s super easy to add your own commands! Just create a python file in
the plugins directory with an ``on_message`` function that returns a
string.

You can use the ``!help`` command to print out all available commands
and a brief help message about them. ``!help <plugin>`` will return just
the help for a particular plugin.

By default, plugins won’t react to messages from other bots (just
messages from humans). Define an ``on_bot_message`` function to handle
bot messages too. See the example plugins for an easy way to define
these functions.

These are the current default plugins:

-  `emoji <https://github.com/llimllib/limbo/wiki/Emoji-Plugin>`__
-  `flip <https://github.com/llimllib/limbo/wiki/Flip-Plugin>`__
-  `gif <https://github.com/llimllib/limbo/wiki/Gif-Plugin>`__
-  `google <https://github.com/llimllib/limbo/wiki/Google-Plugin>`__
-  `help <https://github.com/llimllib/limbo/wiki/Help-Plugin>`__
-  `image <https://github.com/llimllib/limbo/wiki/Image-Plugin>`__
-  `map <https://github.com/llimllib/limbo/wiki/Map-Plugin>`__
-  `poll <https://github.com/llimllib/limbo/wiki/Poll-Plugin>`__
-  `weather <https://github.com/llimllib/limbo/wiki/Weather-Plugin>`__
-  `wiki <https://github.com/llimllib/limbo/wiki/Wiki-Plugin>`__

Contributors
------------

-  `@fsalum <https://github.com/fsalum>`__
-  `@rodvodka <https://github.com/rodvodka>`__
-  `@mattfora <https://github.com/mattfora>`__
-  `@dguido <https://github.com/dguido>`__
-  `@JoeGermuska <https://github.com/JoeGermuska>`__
-  `@MathyV <https://github.com/MathyV>`__
-  `@stopspazzing <https://github.com/stopspazzing>`__
-  `@noise <https://github.com/noise>`__
-  `@drewp <https://github.com/drewp>`__
-  `@TetraEtc <https://github.com/TetraEtc>`__
-  `@LivingInSyn <https://github.com/LivingInSyn>`__
-  `@reversegremlin <https://github.com/reversegremlin>`__
-  `@adamghill <https://github.com/adamghill>`__
-  `@PeterGrace <https://github.com/PeterGrace>`__
-  `@SkiftCreative <https://github.com/SkiftCreative>`__
-  `@diceone <https://github.com/diceone>`__
-  `@rnagle <https://github.com/rnagle>`__
-  `@topher200 <https://github.com/topher200>`__
-  `@StewPoll <https://github.com/StewPoll>`__
-  `@eSoares <https://github.com/eSoares>`__
-  `@sweinstein89 <https://github.com/sweinstein89>`__
-  `@fenwar <https://github.com/fenwar>`__
-  `@rdimartino <https://github.com/rdimartino>`__
