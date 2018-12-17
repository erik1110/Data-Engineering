Last login: Tue Dec 18 01:02:37 on ttys001
➜  ~ git:(master) ✗ cd Desktop/Study/11Git/testgit
➜  testgit git:(master) ls -la
total 0
drwxr-xr-x  3 erik  staff   96 12 18 00:32 .
drwxr-xr-x  6 erik  staff  192 12 18 00:40 ..
drwxr-xr-x  9 erik  staff  288 12 18 01:14 .git
➜  testgit git:(master) more git./config
git./config: No such file or directory
➜  testgit git:(master) more .git/config
[core]
        repositoryformatversion = 0
        filemode = true
        bare = false
        logallrefupdates = true
        ignorecase = true
        precomposeunicode = true
➜  testgit git:(master) find ./
./
.//.git
.//.git/config
.//.git/objects
.//.git/objects/pack
.//.git/objects/info
.//.git/HEAD
.//.git/info
.//.git/info/exclude
.//.git/description
.//.git/hooks
.//.git/hooks/commit-msg.sample
.//.git/hooks/pre-rebase.sample
.//.git/hooks/pre-commit.sample
.//.git/hooks/applypatch-msg.sample
.//.git/hooks/fsmonitor-watchman.sample
.//.git/hooks/pre-receive.sample
.//.git/hooks/prepare-commit-msg.sample
.//.git/hooks/post-update.sample
.//.git/hooks/pre-applypatch.sample
.//.git/hooks/pre-push.sample
.//.git/hooks/update.sample
.//.git/refs
.//.git/refs/heads
.//.git/refs/tags
➜  testgit git:(master) touch test.txt
➜  testgit git:(master) ✗ git add test.txt
➜  testgit git:(master) ✗ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

	new file:   test.txt

➜  testgit git:(master) ✗ find .git
.git
.git/config
.git/objects
.git/objects/pack
.git/objects/info
.git/objects/e6
.git/objects/e6/9de29bb2d1d6434b8b29ae775ad8c2e48c5391
.git/HEAD
.git/info
.git/info/exclude
.git/description
.git/hooks
.git/hooks/commit-msg.sample
.git/hooks/pre-rebase.sample
.git/hooks/pre-commit.sample
.git/hooks/applypatch-msg.sample
.git/hooks/fsmonitor-watchman.sample
.git/hooks/pre-receive.sample
.git/hooks/prepare-commit-msg.sample
.git/hooks/post-update.sample
.git/hooks/pre-applypatch.sample
.git/hooks/pre-push.sample
.git/hooks/update.sample
.git/refs
.git/refs/heads
.git/refs/tags
.git/index
➜  testgit git:(master) ✗ echo "test test test" >> test.txt
➜  testgit git:(master) ✗ cat test.txt
test test test
➜  testgit git:(master) ✗ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

	new file:   test.txt

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   test.txt

➜  testgit git:(master) ✗ git add test.txt
➜  testgit git:(master) ✗ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

	new file:   test.txt

➜  testgit git:(master) ✗ git commit -m "first commit"
[master (root-commit) 2160aa5] first commit
 1 file changed, 1 insertion(+)
 create mode 100644 test.txt
➜  testgit git:(master) touch demo.txt
➜  testgit git:(master) ✗ vim test.txt
➜  testgit git:(master) ✗ more test.txt
test test 
demo demo
➜  testgit git:(master) ✗ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   test.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	demo.txt

no changes added to commit (use "git add" and/or "git commit -a")
➜  testgit git:(master) ✗ git add *
➜  testgit git:(master) ✗ git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	new file:   demo.txt
	modified:   test.txt

➜  testgit git:(master) ✗ git commit -m "second commit"
[master 13c66df] second commit
 2 files changed, 2 insertions(+), 1 deletion(-)
 create mode 100644 demo.txt
➜  testgit git:(master) git log
➜  testgit git:(master) vim .git/config
➜  testgit git:(master) vim demo.txt
➜  testgit git:(master) ✗ git add demo.txt
➜  testgit git:(master) ✗ git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	modified:   demo.txt

➜  testgit git:(master) ✗ git commit -m "edit demo.txt"
[master 1071770] edit demo.txt
 1 file changed, 1 insertion(+)
➜  testgit git:(master) git log
➜  testgit git:(master) 
