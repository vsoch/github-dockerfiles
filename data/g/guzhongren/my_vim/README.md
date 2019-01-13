# vim配置

## 效果

![vim](./img/vim.png)

## 安装

1. clone

```shell
git clone https://github.com/guzhongren/my_vim.git
```

2. 在任意目录进入终端安装 vundle

```shell
git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
```

3. 将 my_vim 目录下的 .vim 和 .vimrc链接到用户目录

```shell
pwd
# ...../my_vim
ln -s /absolute/to/my_vim/.vim  /home/{username}/.vim && ln -s /absolute/to/my_vim/.vimrc  /home/{username}/.vimrc
```

4. 安装插件; 键入vim,进入vim,然后在Normal模式下，键入':PluginInstall'

```shell
vim
# Normal模式
:PluginInstall
```