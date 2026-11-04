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

#### Optional settings

To set up key verification locally, which is not required by GitHub:

```
git config --global gpg.ssh.allowedSignersFile ~/.ssh/allowed_signers
echo  "$(git config --global user.email) $(cat ~/.ssh/id_github_sign.pub)" > ~/.ssh/allowed_signers
```

## Forgot to sign your commits?

Follow the steps below to sign old unsigned commits.

```Bash
# Show commit signature in log
git log --show-signature
```

Identify the unsigned commit and rebase to the commit before it i.e. older than it.

```Bash
# Show commit condensed format
git log --oneline
```

In our case, we will rebase to the commit before our target commit `a27a0fe` which is `906e966`.

```Bash
git rebase -i 906e966^
```

An interactive window will open in your default editor. Replace `pick` with `edit` for the commit(s) in question. Save and close the editor.

You need to do the block of code below n number of times depending on the number n of commits that are unsigned. In our case, we do that twice.

```Bash
git commit --amend --no-edit --gpg-sign
git rebase --continue
```

It is important to note here that you are about to rewrite your Git history 😱. The commit hash of the commits you have amended will literally change.

The `--force-with-lease` flag will allow a force push given your local branch is up-to-date with the remote i.e. no new changes by someone else have been pushed that you have not pulled locally.

```Bash
git push --force-with-lease origin main
```
