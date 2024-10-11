const eth_address = "0x2A43938A365CE6adc69EF718D5fAF1869c261354"

function copy_to_clipboard() {
  navigator.clipboard.writeText(eth_address)
  alert(`ETH adress: ${eth_address} was copied on clipboard!`)
}