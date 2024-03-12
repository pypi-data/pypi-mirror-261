import logging

import borgmatic.borg.check
import borgmatic.config.validate
import borgmatic.hooks.command

logger = logging.getLogger(__name__)


def run_check(
    config_filename,
    repository,
    config,
    hook_context,
    local_borg_version,
    check_arguments,
    global_arguments,
    local_path,
    remote_path,
):
    '''
    Run the "check" action for the given repository.
    '''
    if check_arguments.repository and not borgmatic.config.validate.repositories_match(
        repository, check_arguments.repository
    ):
        return

    borgmatic.hooks.command.execute_hook(
        config.get('before_check'),
        config.get('umask'),
        config_filename,
        'pre-check',
        global_arguments.dry_run,
        **hook_context,
    )
    logger.info(f'{repository.get("label", repository["path"])}: Running consistency checks')
    borgmatic.borg.check.check_archives(
        repository['path'],
        config,
        local_borg_version,
        check_arguments,
        global_arguments,
        local_path=local_path,
        remote_path=remote_path,
    )
    borgmatic.hooks.command.execute_hook(
        config.get('after_check'),
        config.get('umask'),
        config_filename,
        'post-check',
        global_arguments.dry_run,
        **hook_context,
    )
