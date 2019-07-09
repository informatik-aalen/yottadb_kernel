YottaDB-kernel for jupyter notebook

1) Install jupyter notebook
2) In bash: Go to directory yottadbkernel and type
==> jupyter kernelspec install --user yottadb/
3) You can check in bash:
==> jupyter kernelspec list
yottadb shoul be printed
4) Your YottaDB-env-variables must be set!
==> $ydb_dist/ydb
must work!
5) Start jupyter notebook in this yottadbkernel-directory
Alt. copy yottadbkernel.py to your yottadb-routine-dir and start jupyter notebook there!
(Then all M-Routines are listed and can be edited)
