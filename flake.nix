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

        pythonWithPygame = pkgs.python313.withPackages (ps: [
          ps.pygame
        ]);

      in
      {
        devShells.default = pkgs.mkShell {
          name = "pygame-pdm-env";

          packages = [
            pythonWithPygame
            pkgs.pdm
            pkgs.uv

            pkgs.SDL2
            pkgs.SDL2_image
            pkgs.SDL2_mixer
            pkgs.SDL2_ttf
            pkgs.SDL2_gfx
          ];

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
