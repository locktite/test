#! /bin/bash

BACKUP_DIR="/backup"
USER=$(whoami)
DATE=$(date +%Y-%m-%d)
ENV_BACKUP_FILE="$BACKUP_DIR/$USER-$DATE-Env-Backup.tgz"
BACKUP_FILE="$BACKUP_DIR/$USER-$DATE-Backup.tgz"


function create_env_backup {
  echo "Compress files to $BACKUP_FILE"
  tar -czf $ENV_BACKUP_FILE -C $HOME .bashrc .ssh/authorized_keys path.txt printenv.txt

}


function create_backup {
  echo "Compress files to $BACKUP_FILE"
  tar -czf $BACKUP_FILE -C $HOME .

}

function create_backup_dir {
  mkdir -p $BACKUP_DIR
}

function export_envdata {
  printenv > printenv.txt
  echo $PATH > path.txt
}

function print_message {
  echo "Backup complete: $BACKUP_FILE"
}

create_backup_dir
create_env_backup
create_backup
print_message


