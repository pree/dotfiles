# Path to your oh-my-zsh installation.
export ZSH=$HOME/.oh-my-zsh

ZSH_THEME="agnoster"

plugins=(git)

source $ZSH/oh-my-zsh.sh

# User configuration

export EDITOR='vim'
export TERMINAL='termite'
export GPG_TTY=$(tty)
export LC_ALL=en_US.UTF-8

alias git_sync='find -mindepth 1 -maxdepth 1 -type d -exec echo -e "\033[0;32mPulling " {} "\033[0;0m" \; -exec git -C {} pull \;'

if [ "$(tty)" = "/dev/tty1" ]; then
   startx
fi
