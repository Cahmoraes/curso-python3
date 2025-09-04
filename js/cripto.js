import crypto from 'crypto'

const secret = 'minha_chave_secreta'

// Gerar HMAC
function gerarHmac(payload) {
  return crypto.createHmac('sha256', secret).update(payload).digest('hex')
}

// Verificar HMAC
function verificarHmac(payload, recebido) {
  const esperado = gerarHmac(payload)
  return crypto.timingSafeEqual(
    Buffer.from(esperado, 'hex'),
    Buffer.from(recebido, 'hex'),
  )
}

// Testando
const msg = 'dados-importantes'
const assinatura = gerarHmac(msg)

console.log('Assinatura:', assinatura)
console.log('Validação correta:', verificarHmac(msg, assinatura))
console.log('Validação errada:', verificarHmac(msg, '123456'))
