package com.times.jogadores.jogadores;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import jakarta.transaction.Transactional;

@RestController
@RequestMapping("/jogadores")
public class JogadorController {

	@Autowired
	private JogadorRepository repository;
	
	@GetMapping
	public List<Jogador> listar() {
		return repository.findAll();
	}
	
	@PostMapping
	@Transactional
	public void criar(@RequestBody DadosCadastroJogador dados) {
		repository.save(new Jogador(dados));
	}
	
}
