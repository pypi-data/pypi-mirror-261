#!/bin/bash

INPUT=$1
GENERATE_COUNT=$2
DEFAULT_GENERATE_COUNT=10000

function run(){
  echo "输入参数为 $INPUT $GENERATE_COUNT"
  mkdir gbk
  mkdir out
  generateData
}

function generateData() {
  # 判断生成数量是否存在,不存在则给默认值10000
  if [ $GENERATE_COUNT -eq 0 ];then
    $GENERATE_COUNT=$DEFAULT_GENERATE_COUNT
  fi
  transDataDir
  # 如果输入参数是文件，则直接调用jar
  if [ -f $INPUT ];then
    callJar $INPUT $GENERATE_COUNT
  # 如果输入参数是文件夹，则遍历该文件夹下的内容，每个调用jar
  elif [ -d $INPUT ]; then
    for file in $(ls $1 | grep abnf$)
    do
    callJar $file $GENERATE_COUNT
    done
  else
    echo "输入参数非文件,也非文件夹"
  fi
}

# 调用jar包
function callJar() {
  input=$1
  count=$2
  echo "开始处理文件$input"
  output=$1_out
  iconv -f utf-8 -t gbk $input > gbk/$input.gbk
  java -jar ../Generator.jar -generate $count -file gbk/$input.gbk -output gbk/$output.gbk
  iconv -f gbk -t utf-8 gbk/$output.gbk > out/outtmp
  sort out/outtmp | uniq >out/$output
  echo "处理文件结束$input"
}

# 转换数据文件夹里的字典
function transDataDir() {
  dataPath=$INPUT/data/
  if [ -d $dataPath ]; then
    echo "ok"
    trans $dataPath
  fi
}

#转换数据
function trans() {
  dics=`ls $INPUT/data`
  if [ ! -d $1/.temp_gbk ]; then
    mkdir $1/.temp_gbk
  fi
  for dic in $dics
  do
    file=$INPUT/data/$dic
    if [[ "$file" =~ gbk$ ]];then
      echo $file
    else
      if [ -f "$file" ];then
        iconv -f utf-8 -t gbk -c $file > $1/.temp_gbk/$dic.gbk
      fi
    fi
  done
  mv $1/.temp_gbk/* $1
}

run