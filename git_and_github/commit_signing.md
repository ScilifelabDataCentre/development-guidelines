# Commit signing

## Configuring commit signing

_These instructions assume that you have already installed git._

Git commits can be signed using e.g. GPG or SSH keys. All software required for SSH keys is installed by default on
most computers, while GPG may require some software to be installed. Use an SSH key by default.

1. [Follow the instructions for your operating system in the GitHub Docs](https://docs.github.com/en/authentication/managing-commit-signature-verification/about-commit-signature-verification#ssh-commit-signature-verification)
   - Use an informative name when generating the SSH key (e.g. `id_github_sign`)
   - When adding the generated key to your GitHub account via the GitHub interface, change the key type to be _Signing_.
2. To sign your commits automatically with `git commit` (rather than using `git commit -S`):

```
git config --global commit.gpgsign true
git config --global tag.gpgsign true
```

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
