import { Configuration, OpenAIApi } from "openai";
import { configDotenv } from "dotenv";

configDotenv()

const config = new Configuration({
  apiKey: process.env.OPENAI_API_KEY
})

const openai = new OpenAIApi(config)

try {
  const { data: { choices: responses } } = await openai.createCompletion({
    model: "text-davinci-003",
    prompt: "Hi, how are you?",
    temperature: 1,
    max_tokens: 256,
    top_p: 1,
    frequency_penalty: 0,
    presence_penalty: 0,
  })

  console.log(responses[0].text)
} catch (error) {
  console.log(error.response)
}
