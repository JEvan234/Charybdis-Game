{
  description = "JEvan234/Charybdis-Game NIX development environment using PDM";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };

        python = pkgs.python313;

        pygame-sys-deps = with pkgs; [
          SDL2
          (SDL2_image.overrideAttrs (oldAttrs: {
            buildInputs = oldAttrs.buildInputs ++ [ libpng libjpeg libwebp ];
          }))          
	  SDL2_mixer
          SDL2_ttf
          SDL2_gfx
          pkg-config
          xorg.libX11
          xorg.libXext
          xorg.libXrandr
        ];

      in
      {
        devShells.default = pkgs.mkShell {
          name = "pygame-pdm-env";

          packages = [
            python
            pkgs.pdm
            pkgs.uv
          ] ++ pygame-sys-deps;

          shellHook = ''
            export PDM_VENV_IN_PROJECT=1
            pdm use python
            pdm install
            source .venv/bin/activate
          '';
        };
      }
    );
}


