#MINSIZE：データの最小サイズ、MAX_SIZE：データの最大サイズ、STEP_SIZE：刻み幅
#MAX_SIZEとSTEP_SIZEが同じ場合は1回だけpingコマンドを実行する。

$MIN_SIZE = 1472
$MAX_SIZE = 1472
$STEP_SIZE = 1472
$ONLY_ONCE = $false
$IP_ADDRESS = "8.8.8.8"
$PING_MAX_COUNT = 2
$LOG_DIR = "${PSScriptRoot}\test_${IP_ADDRESS}_${MIN_SIZE}_${MAX_SIZE}_${STEP_SIZE}"



if((Test-Path $LOG_DIR) -eq $true){
  Remove-Item $LOG_DIR -Recurse
}

New-Item ${LOG_DIR} -ItemType Directory


if(${MAX_SIZE} -eq ${STEP_SIZE}){
  $MAX_COUNT = 1
}
elseif(${ONLY_ONCE})
{
  $MAX_COUNT = 1
}
else{
  $MAX_COUNT = (${MAX_SIZE} - ${MIN_SIZE})/${STEP_SIZE} + 1
}


for ($i=0; $i -lt ${MAX_COUNT}; $i++){
  $DATA_SIZE = $MIN_SIZE + ${STEP_SIZE} * ${i}
  $LOG_FILE = "${LOG_DIR}\ping_${IP_ADDRESS}_${MIN_SIZE}_${MAX_SIZE}_${STEP_SIZE}_${DATA_SIZE}.log"

  ping "${IP_ADDRESS}" -l ${DATA_SIZE} -f -n ${PING_MAX_COUNT}| Tee-Object -FilePath ${LOG_FILE}
}