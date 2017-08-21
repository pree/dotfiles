# Path to your oh-my-zsh installation.
export ZSH=/home/schizopriest/.oh-my-zsh

ZSH_THEME="agnoster"

plugins=(git)

source $ZSH/oh-my-zsh.sh

# User configuration

export EDITOR='vim'
export GPG_TTY=$(tty)
export LC_ALL=en_US.UTF-8

if [ "$(tty)" = "/dev/tty1" ]; then
   startx
fi
