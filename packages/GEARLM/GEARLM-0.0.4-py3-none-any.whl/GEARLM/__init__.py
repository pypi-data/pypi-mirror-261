
from .TrueCompression.models.TrueCompressLlama import GearlamaForCausalLMNew
from .TrueCompression.old_models.modeling_llama_old import GearlamaForCausalLM

from .Simulated.compress_config import CompressionConfig
from .Simulated.modeling_llama_new import SimulatedGearLlamaForCausalLM
# from .modeling_llama_h2o import H2OLlamaForCausalLM, LlamaConfig
from .Simulated.modeling_mistral import SimulatedGearMistralForCausalLM, MistralConfig
from .Simulated.h2o_llama_self_written import LlamaForCausalLMH2O
