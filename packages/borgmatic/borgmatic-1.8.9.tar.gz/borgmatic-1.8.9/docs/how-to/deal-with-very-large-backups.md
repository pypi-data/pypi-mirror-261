---
title: How to deal with very large backups
eleventyNavigation:
  key: 📏 Deal with very large backups
  parent: How-to guides
  order: 4
---
## Biggish data

Borg itself is great for efficiently de-duplicating data across successive
backup archives, even when dealing with very large repositories. But you may
find that while borgmatic's default actions of `create`, `prune`, `compact`,
and `check` works well on small repositories, it's not so great on larger
ones. That's because running the default pruning, compact, and consistency
checks take a long time on large repositories.

<span class="minilink minilink-addedin">Prior to version 1.7.9</span> The
default action ordering was `prune`, `compact`, `create`, and `check`.

### A la carte actions

If you find yourself wanting to customize the actions, you have some options.
First, you can run borgmatic's `prune`, `compact`, `create`, or `check`
actions separately. For instance, the following optional actions are
available (among others):

```bash
borgmatic create
borgmatic prune
borgmatic compact
borgmatic check
```

You can run borgmatic with only one of these actions provided, or you can mix
and match any number of them in a single borgmatic run. This supports
approaches like skipping certain actions while running others. For instance,
this skips `prune` and `compact` and only runs `create` and `check`:

```bash
borgmatic create check
```

<span class="minilink minilink-addedin">New in version 1.7.9</span> borgmatic
now respects your specified command-line action order, running actions in the
order you specify. In previous versions, borgmatic ran your specified actions
in a fixed ordering regardless of the order they appeared on the command-line.

But instead of running actions together, another option is to run backups with
`create` on a frequent schedule (e.g. with `borgmatic create` called from one
cron job), while only running expensive consistency checks with `check` on a
much less frequent basis (e.g. with `borgmatic check` called from a separate
cron job).

<span class="minilink minilink-addedin">New in version 1.8.5</span> Instead of
(or in addition to) specifying actions on the command-line, you can configure
borgmatic to [skip particular
actions](https://torsion.org/borgmatic/docs/how-to/set-up-backups/#skipping-actions).


### Consistency check configuration

Another option is to customize your consistency checks. By default, if you
omit consistency checks from configuration, borgmatic runs full-repository
checks (`repository`) and per-archive checks (`archives`) within each
repository. (Although see below about check frequency.) This is equivalent to
what `borg check` does if run without options.

But if you find that archive checks are too slow, for example, you can
configure borgmatic to run repository checks only. Configure this in the
`consistency` section of borgmatic configuration:

```yaml
checks:
    - name: repository
```

<span class="minilink minilink-addedin">Prior to version 1.8.0</span> Put
this option in the `consistency:` section of your configuration.

<span class="minilink minilink-addedin">Prior to version 1.6.2</span> The
`checks` option was a plain list of strings without the `name:` part, and
borgmatic ran each configured check every time checks were run. For example:

```yaml
checks:
    - repository
```


Here are the available checks from fastest to slowest:

 * `repository`: Checks the consistency of the repository itself.
 * `archives`: Checks all of the archives in the repository.
 * `extract`: Performs an extraction dry-run of the most recent archive.
 * `data`: Verifies the data integrity of all archives contents, decrypting and decompressing all data.

Note that the `data` check is a more thorough version of the `archives` check,
so enabling the `data` check implicitly enables the `archives` check as well.

See [Borg's check
documentation](https://borgbackup.readthedocs.io/en/stable/usage/check.html)
for more information.


### Check frequency

<span class="minilink minilink-addedin">New in version 1.6.2</span> You can
optionally configure checks to run on a periodic basis rather than every time
borgmatic runs checks. For instance:

```yaml
checks:
    - name: repository
      frequency: 2 weeks
    - name: archives
      frequency: 1 month
```

<span class="minilink minilink-addedin">Prior to version 1.8.0</span> Put
this option in the `consistency:` section of your configuration.

This tells borgmatic to run the `repository` consistency check at most once
every two weeks for a given repository and the `archives` check at most once a
month. The `frequency` value is a number followed by a unit of time, e.g. `3
days`, `1 week`, `2 months`, etc. The set of possible time units is as
follows (singular or plural):

 * `second`
 * `minute`
 * `hour`
 * `day`
 * `week` (7 days)
 * `month` (30 days)
 * `year` (365 days)

The `frequency` defaults to `always` for a check configured without a
`frequency`, which means run this check every time checks run. But if you omit
consistency checks from configuration entirely, borgmatic runs full-repository
checks (`repository`) and per-archive checks (`archives`) within each
repository, at most once a month.

Unlike a real scheduler like cron, borgmatic only makes a best effort to run
checks on the configured frequency. It compares that frequency with how long
it's been since the last check for a given repository (as recorded in a file
within `~/.borgmatic/checks`). If it hasn't been long enough, the check is
skipped. And you still have to run `borgmatic check` (or `borgmatic` without
actions) in order for checks to run, even when a `frequency` is configured!

This also applies *across* configuration files that have the same repository
configured. Make sure you have the same check frequency configured in each
though—or the most frequently configured check will apply.

If you want to temporarily ignore your configured frequencies, you can invoke
`borgmatic check --force` to run checks unconditionally.

<span class="minilink minilink-addedin">New in version 1.8.6</span> `borgmatic
check --force` runs `check` even if it's specified in the `skip_actions`
option.


### Running only checks

<span class="minilink minilink-addedin">New in version 1.7.1</span> If you
would like to only run consistency checks without creating backups (for
instance with the `check` action on the command-line), you can omit
the `source_directories` option entirely.

<span class="minilink minilink-addedin">Prior to version 1.7.1</span> In older
versions of borgmatic, instead specify an empty `source_directories` value, as
it is a mandatory option there:

```yaml
location:
    source_directories: []
```


### Disabling checks

If that's still too slow, you can disable consistency checks entirely,
either for a single repository or for all repositories.

<span class="minilink minilink-addedin">New in version 1.8.5</span> Disabling
all consistency checks looks like this:

```yaml
skip_actions:
    - check
```

<span class="minilink minilink-addedin">Prior to version 1.8.5</span> Use this
configuration instead:

```yaml
checks:
    - name: disabled
```

<span class="minilink minilink-addedin">Prior to version 1.8.0</span> Put
`checks:` in the `consistency:` section of your configuration.

<span class="minilink minilink-addedin">Prior to version 1.6.2</span>
`checks:` was a plain list of strings without the `name:` part. For instance:

```yaml
checks:
    - disabled
```

If you have multiple repositories in your borgmatic configuration file,
you can keep running consistency checks, but only against a subset of the
repositories:

```yaml
check_repositories:
    - path/of/repository_to_check.borg
```

Finally, you can override your configuration file's consistency checks and
run particular checks via the command-line. For instance:

```bash
borgmatic check --only data --only extract
```

This is useful for running slow consistency checks on an infrequent basis,
separate from your regular checks. It is still subject to any configured
check frequencies unless the `--force` flag is used.


## Troubleshooting

### Broken pipe with remote repository

When running borgmatic on a large remote repository, you may receive errors
like the following, particularly while "borg check" is validating backups for
consistency:

```text
    Write failed: Broken pipe
    borg: Error: Connection closed by remote host
```

This error can be caused by an ssh timeout, which you can rectify by adding
the following to the `~/.ssh/config` file on the client:

```text
    Host *
        ServerAliveInterval 120
```

This should make the client keep the connection alive while validating
backups.
