package shim

import (
	"github.com/hashicorp/terraform-plugin-framework/provider"

	p "github.com/prefecthq/terraform-provider-prefect/internal/provider"
)

func NewProvider() provider.Provider {
	return p.New()
}
