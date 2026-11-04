---
last_reviewed: 2026-11-04
---

# Commit signing

- Recommended
- Why

Git commits can be signed using e.g. GPG or SSH keys. All software required for SSH keys is installed by default on
most computers, while GPG may require some software to be installed. Use an SSH key by default.

## How to configure commit signing

> [!NOTE]
> These instructions assume that you have already installed git.

To set up commit signing, follow the instructions in the GitHub Docs:

- [SSH commit signature verification](https://docs.github.com/en/authentication/managing-commit-signature-verification/about-commit-signature-verification#ssh-commit-signature-verification)
- [GPG commit signature verification](https://docs.github.com/en/authentication/managing-commit-signature-verification/about-commit-signature-verification#gpg-commit-signature-verification)

### How to enable automatic signing of commits

To sign new changes, you could use the command `git commit -S`. However, this requires you to remember the `-S` option.

To configure automatic signing of commits, run the following command:

```bash
git config --global commit.gpgsign true
```

After this, you should be able to make a change, run `git commit` (no `-S`) and be automatically prompted for your passphrase.

> [!NOTE]
> You can also configure git to automatically sign tags:
>
> ```bash
> git config --global tag.gpgsign true
> ```

### Optional settings

To set up key verification locally, which is not required by GitHub:

```bash
git config --global gpg.ssh.allowedSignersFile ~/.ssh/allowed_signers
echo  "$(git config --global user.email) $(cat ~/.ssh/id_github_sign.pub)" > ~/.ssh/allowed_signers
```

## Forgot to sign your commits?

1. To sign unsigned commits in your current branch, run the following command, replacing `<base>` with your base branch.

   > [!WARNING]
   > You are about to rewrite your Git history. The commit hashes will change.

   ```bash
   git rebase --exec 'git commit --amend --no-edit -S' <base>

   # Example: You've created your branch from `main` / signing commits in a PR to `main`.
   git rebase --exec 'git commit --amend --no-edit -S' main
   ```

2. Push to your remote branch with the `--force-with-lease` flag. It will allow a force push given that your localm branch is up-to-date with the remote.

   ```Bash
   git push --force-with-lease origin main
   ```
